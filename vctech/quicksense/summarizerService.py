import re
from youtube_transcript_api import YouTubeTranscriptApi
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from vctech.settings import OPENAI_KEY
from .prompts import SYSTEM_PROMPT, USER_PROMPT, MAP_PROMPT_TEMPLATE,COMBINE_PROMPT_TEMPLATE
from youtube_transcript_api._errors import NoTranscriptFound
from .responses import Errors, ErrorResponse
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.llms import OpenAI as LC_OPENAI
class Summarizer():

    def __init__(self, id, link):
        self.video_id = id
        self.link = link
        self.client = OpenAI(api_key=OPENAI_KEY)
        self.llm = LC_OPENAI(openai_api_key=OPENAI_KEY)
        self.model = "gpt-3.5-turbo-16k"
        self.transcript = None

    def getTitle(self):
        r = requests.get(self.link)
        soup = BeautifulSoup(r.text)
        titles = soup.find_all(name="title")[0]
        title = str(titles)
        title = title.replace("<title>", "")
        title = title.replace("</title>", "")
        title = title.replace("- YouTube", "")
        return title

    def format_time(self, time):
        hours, remainder = divmod(time, 3600)
        minutes, seconds = divmod(remainder, 60)
        if (hours == 0):
            return f'{int(minutes):02d}:{int(seconds):02d}'
        else:
            return f'{int(hours):02d}:{int(minutes):02d}'

    def getTransScript(self):
        if (self.transcript == None):
            transcript_list = YouTubeTranscriptApi.list_transcripts(
                self.video_id)
            try:
                transcript = transcript_list.find_transcript(['en'])
            except NoTranscriptFound:
                return Errors.NO_TRANSCRIPT

            transcript_data = transcript.fetch()
            outputJsonArray = []
            chunk_duration = 20
            chunk_start = 0
            chunk_text = ""

            for line in transcript_data:
                if line['start'] < chunk_start + chunk_duration:
                    chunk_text += line['text'] + " "
                else:
                    end_time = chunk_start + chunk_duration
                    start_time_formatted = self.format_time(chunk_start)
                    objJson = {
                        "start": start_time_formatted,
                        "text": chunk_text.strip()
                    }
                    outputJsonArray.append(objJson)
                    chunk_start = end_time
                    chunk_text = line['text'] + " "
            if chunk_text:
                end_time = chunk_start + chunk_duration
                start_time_formatted = self.format_time(chunk_start)
                objJson = {
                    "start": start_time_formatted,
                    "text": chunk_text.strip()
                }
                outputJsonArray.append(objJson)
            self.transcript = outputJsonArray

        # To do
        duration_in_minutes = 30
        return self.transcript, duration_in_minutes

    def extract_entities(self):
        title = self.getTitle()
        transcripts = self.getTransScript()
        if (transcripts == Errors.NO_TRANSCRIPT):
            return transcripts, transcripts, transcripts
        transcript = [o["text"] for o in transcripts]
        return title, (" ").join(transcript), transcripts

    def GPT(self, transcript, title):
        completion = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": USER_PROMPT.format(transcript=transcript, title=title)
                }
            ]
        )
        return completion.choices[0].message.content

    def largeSumarizer(self):
        content = ("\n").join([t["text"] for t in self.transcripts])
        text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n"], chunk_size=5000, chunk_overlap=250)
        docs = text_splitter.create_documents([content])
        summary_chain = load_summarize_chain(llm=self.llm,
                                     chain_type='map_reduce',
                                     map_prompt=MAP_PROMPT_TEMPLATE,
                                     combine_prompt=COMBINE_PROMPT_TEMPLATE,
                                    )
        output = summary_chain.run(docs)
        return output 


    def summarise(self):
        title, transcript, transcripts = self.extract_entities()
        if (title == Errors.NO_TRANSCRIPT):
            return ErrorResponse.NO_TRANSCRIPT_CODE
        else:
            content_length = self.llm.get_num_tokens(transcript)
            if(content_length>9000):
                summary = self.largeSumarizer()
                response = {
                    "title": title,
                    "transscript": transcripts,
                    "summary": summary
                }
            else:
                summary = self.GPT(title, transcript)
                response = {
                    "title": title,
                    "transscript": transcripts,
                    "summary": summary
                }
        return response
