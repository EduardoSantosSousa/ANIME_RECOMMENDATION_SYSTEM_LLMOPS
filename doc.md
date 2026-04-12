ANIME_RECOMMENDER/
│
├── ANIME_RECOMMENDER.egg-info/
│
├── app/
│ ├── init.py
│ └── app.py
│
├── chroma_db/
│ ├── 3c159568-24c6-48b0-b119-a56ef9a4700b/
│ └── chroma.sqlite3
│
├── config/
│ ├── pycache/
│ ├── init.py
│ └── config.py
│
├── data/
│ ├── anime_updated.csv
│ └── anime_with_synopsis.csv
│
├── doc/
│ ├── code.html
│ ├── DESIGN.md
│ └── screen.png
│
├── logs/
│ └── log_2026-04-11.log
│
├── pipeline/
│ ├── pycache/
│ ├── init.py
│ ├── build_pipeline.py
│ └── pipeline.py
│
├── src/
│ ├── pycache/
│ ├── init.py
│ ├── data_loader.py
│ ├── prompt_template.py
│ ├── recommender.py
│ └── vector_store.py
│
├── static/
│ └── js/
│ └── app.js
│
├── templates/
│ └── index.html
│
├── utils/
│ ├── pycache/
│ └── custom_exception.py
│
├── logger.py
├── venv/
├── .env
├── api.py
├── doc.md
├── requirements.txt
└── setup.py

app.py: 

import streamlit as st
from pipeline.pipeline import AnimeRecommendationPipeline
from dotenv import load_dotenv

st.set_page_config(page_title="Anime Recommender", layout="wide")

load_dotenv()

@st.cache_resource
def init_pipeline():
    return AnimeRecommendationPipeline()

pipeline = init_pipeline()

st.title("Anime Recommender System")
query = st.text_input("Enter your anime preferences eg.:  light hearted anime with school settings")
if query:
    with st.spinner("Fetching recommendations for you....."):
        response = pipeline.recommend(query)
        st.markdown("### Recommendations")
        st.write(response)  

config.py: 

import os 
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.1-8b-instant"

anime_updated.csv: 
combined_info
"Title: Cowboy Bebop.. Overview: In the year 2071, humanity has colonized several of the planets and moons of the solar system leaving the now uninhabitable surface of planet Earth behind. The Inter Solar System Police attempts to keep peace in the galaxy, aided in part by outlaw bounty hunters, referred to as ""Cowboys."" The ragtag team aboard the spaceship Bebop are two such individuals. Mellow and carefree Spike Spiegel is balanced by his boisterous, pragmatic partner Jet Black as the pair makes a living chasing bounties and collecting rewards. Thrown off course by the addition of new members that they meet in their travels—Ein, a genetically engineered, highly intelligent Welsh Corgi; femme fatale Faye Valentine, an enigmatic trickster with memory loss; and the strange computer whiz kid Edward Wong—the crew embarks on thrilling adventures that unravel each member's dark and mysterious past little by little. Well-balanced with high density action and light-hearted comedy, Cowboy Bebop is a space Western classic and an homage to the smooth and improvised music it is named after.Genres: Action, Adventure, Comedy, Drama, Sci-Fi, Space"
"Title: Cowboy Bebop: Tengoku no Tobira.. Overview: other day, another bounty—such is the life of the often unlucky crew of the Bebop. However, this routine is interrupted when Faye, who is chasing a fairly worthless target on Mars, witnesses an oil tanker suddenly explode, causing mass hysteria. As casualties mount due to a strange disease spreading through the smoke from the blast, a whopping three hundred million woolong price is placed on the head of the supposed perpetrator. With lives at stake and a solution to their money problems in sight, the Bebop crew springs into action. Spike, Jet, Faye, and Edward, followed closely by Ein, split up to pursue different leads across Alba City. Through their individual investigations, they discover a cover-up scheme involving a pharmaceutical company, revealing a plot that reaches much further than the ragtag team of bounty hunters could have realized.Genres: Action, Drama, Mystery, Sci-Fi, Space"
"Title: Trigun.. Overview: Vash the Stampede is the man with a $$60,000,000,000 bounty on his head. The reason: he's a merciless villain who lays waste to all those that oppose him and flattens entire cities for fun, garnering him the title ""The Humanoid Typhoon."" He leaves a trail of death and destruction wherever he goes, and anyone can count themselves dead if they so much as make eye contact—or so the rumors say. In actuality, Vash is a huge softie who claims to have never taken a life and avoids violence at all costs. With his crazy doughnut obsession and buffoonish attitude in tow, Vash traverses the wasteland of the planet Gunsmoke, all the while followed by two insurance agents, Meryl Stryfe and Milly Thompson, who attempt to minimize his impact on the public. But soon, their misadventures evolve into life-or-death situations as a group of legendary assassins are summoned to bring about suffering to the trio. Vash's agonizing past will be unraveled and his morality and principles pushed to the breaking point.Genres: Action, Sci-Fi, Adventure, Comedy, Drama, Shounen"

C:\Users\z004hn4c\Documents\Estudo\LLMOps And AIOps Bootcamp With 8 End To End Projects\anime_recomender_project\data\anime_with_synopsis.csv:
MAL_ID,Name,Score,Genres,sypnopsis
1,Cowboy Bebop,8.78,"Action, Adventure, Comedy, Drama, Sci-Fi, Space","In the year 2071, humanity has colonized several of the planets and moons of the solar system leaving the now uninhabitable surface of planet Earth behind. The Inter Solar System Police attempts to keep peace in the galaxy, aided in part by outlaw bounty hunters, referred to as ""Cowboys."" The ragtag team aboard the spaceship Bebop are two such individuals. Mellow and carefree Spike Spiegel is balanced by his boisterous, pragmatic partner Jet Black as the pair makes a living chasing bounties and collecting rewards. Thrown off course by the addition of new members that they meet in their travels—Ein, a genetically engineered, highly intelligent Welsh Corgi; femme fatale Faye Valentine, an enigmatic trickster with memory loss; and the strange computer whiz kid Edward Wong—the crew embarks on thrilling adventures that unravel each member's dark and mysterious past little by little. Well-balanced with high density action and light-hearted comedy, Cowboy Bebop is a space Western classic and an homage to the smooth and improvised music it is named after."
5,Cowboy Bebop: Tengoku no Tobira,8.39,"Action, Drama, Mystery, Sci-Fi, Space","other day, another bounty—such is the life of the often unlucky crew of the Bebop. However, this routine is interrupted when Faye, who is chasing a fairly worthless target on Mars, witnesses an oil tanker suddenly explode, causing mass hysteria. As casualties mount due to a strange disease spreading through the smoke from the blast, a whopping three hundred million woolong price is placed on the head of the supposed perpetrator. With lives at stake and a solution to their money problems in sight, the Bebop crew springs into action. Spike, Jet, Faye, and Edward, followed closely by Ein, split up to pursue different leads across Alba City. Through their individual investigations, they discover a cover-up scheme involving a pharmaceutical company, revealing a plot that reaches much further than the ragtag team of bounty hunters could have realized."
6,Trigun,8.24,"Action, Sci-Fi, Adventure, Comedy, Drama, Shounen","Vash the Stampede is the man with a $$60,000,000,000 bounty on his head. The reason: he's a merciless villain who lays waste to all those that oppose him and flattens entire cities for fun, garnering him the title ""The Humanoid Typhoon."" He leaves a trail of death and destruction wherever he goes, and anyone can count themselves dead if they so much as make eye contact—or so the rumors say. In actuality, Vash is a huge softie who claims to have never taken a life and avoids violence at all costs. With his crazy doughnut obsession and buffoonish attitude in tow, Vash traverses the wasteland of the planet Gunsmoke, all the while followed by two insurance agents, Meryl Stryfe and Milly Thompson, who attempt to minimize his impact on the public. But soon, their misadventures evolve into life-or-death situations as a group of legendary assassins are summoned to bring about suffering to the trio. Vash's agonizing past will be unraveled and his morality and principles pushed to the breaking point."

build_pipeline.py: 

from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)

def main():
    try:
        logger.info("Starting to build pipeline...")

        loader = AnimeDataLoader("data/anime_with_synopsis.csv", "data/anime_updated.csv")
        processed_csv = loader.load_and_process()

        logger.info("Data loaded and processed...")

        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstore()

        logger.info("Vector store Build sucesfully....")

        logger.info("Pipeline build sucesfully....")

    except Exception as e:
        logger.error(f"Failed to execute pipeline {str(e)}")
        raise CustomException("Error during pipeline initialized", e)
    

if __name__=="__main__":
    main()

pipeline.py:

from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import GROQ_API_KEY, MODEL_NAME
from utils.logger import get_logger
from  utils.custom_exception import CustomException

logger = get_logger(__name__)

class AnimeRecommendationPipeline:
    def __init__(self, persist_dir = "chroma_db"):
        try:
            logger.info("Initializing Recommendation Pipeline")

            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)

            retriever = vector_builder.load_vector_store().as_retriever()

            self.recommender = AnimeRecommender(retriever, GROQ_API_KEY, MODEL_NAME)

            logger.info("Pipeline intialized sucesfully...")

        except Exception as e:
            logger.error(f"Failed to initialize pipeline {str(e)}")
            raise CustomException("Error during pipeline initialization", e)

    def recommend(self, query:str) -> str:
        try:
            logger.info(f"Recived a query {query}")

            recommendation = self.recommender.get_recommendation(query)

            logger.info("Recommendation generated sucesfuly...")

            return recommendation

        except Exception as e:
            logger.error(f"Failed to get recommendation {str(e)}")
            raise CustomException("Error during getting recommendation", e)

data_loader.py: 

import pandas as pd 

class AnimeDataLoader:
    
    def __init__(self, original_csv:str, processed_csv:str):
        self.original_csv = original_csv
        self.processed_csv = processed_csv

    def load_and_process(self):
        df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna()

        required_cols = {'Name', 'Genres', 'sypnopsis'}

        missing = required_cols - set(df.columns)

        if missing:
            raise ValueError('Missing column in CSV File')

        df['combined_info'] = (
            "Title: " + df["Name"] + ".. Overview: " + df["sypnopsis"] + "Genres: " + df["Genres"]
        )

        df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')

        return self.processed_csv

prompt_template.py: 

from langchain_core.prompts import PromptTemplate

def get_anime_prompt():
    template = """
You are an expert anime recommender. Your job is to help users find the perfect anime based on their preferences.

Using the following context, provide a detailed and engaging response to the user's question.

For each question, suggest exactly three anime titles. For each recommendation, include:
1. The anime title.
2. A concise plot summary (2-3 sentences).
3. A clear explanation of why this anime matches the user's preferences.

Present your recommendations in a numbered list format for easy reading.

If you don't know the answer, respond honestly by saying you don't know — do not fabricate any information.

Context:
{context}

User's question:
{question}

Your well-structured response:
"""

    return PromptTemplate(template=template, input_variables=["context", "question"])

recommender.py: 

from langchain_classic.chains.retrieval_qa.base import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )

    def get_recommendation(self, query: str):
        result = self.qa_chain.invoke({"query": query})
        return result['result']

vector_store.py:

from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_path: str, persist_dir: str = 'chroma_db'):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    def build_and_save_vectorstore(self):
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding='utf-8',
            metadata_columns=[]
        )

        data = loader.load()

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.split_documents(data)

        db = Chroma.from_documents(texts, self.embedding, persist_directory=self.persist_dir)
        db.persist()

    def load_vector_store(self):
        return Chroma(persist_directory=self.persist_dir, embedding_function=self.embedding)

index.html: 

<!DOCTYPE html>

<html class="dark" lang="en"><head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>PULSE.AI | Find Your Next Obsession</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&amp;family=Manrope:wght@300;400;500;600;700&amp;display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&amp;display=swap" rel="stylesheet"/>
<script id="tailwind-config">
      tailwind.config = {
        darkMode: "class",
        theme: {
          extend: {
            "colors": {
                    "primary-fixed-dim": "#ff586c",
                    "background": "#040e1f",
                    "secondary-container": "#944a00",
                    "inverse-surface": "#f9f9ff",
                    "outline-variant": "#3d485c",
                    "error-container": "#9f0519",
                    "outline": "#6b768b",
                    "on-tertiary-fixed": "#373f54",
                    "tertiary-fixed": "#dae2fd",
                    "secondary-fixed": "#ffc69f",
                    "on-secondary-fixed-variant": "#7f3f00",
                    "surface-container-low": "#061326",
                    "surface-container": "#0b1a2f",
                    "surface-dim": "#040e1f",
                    "surface-bright": "#1b2c47",
                    "on-tertiary": "#525a70",
                    "on-secondary": "#4c2300",
                    "on-primary-fixed-variant": "#5f0017",
                    "on-secondary-container": "#fff6f2",
                    "on-secondary-fixed": "#552800",
                    "inverse-primary": "#bf0037",
                    "tertiary-dim": "#ccd4ee",
                    "on-primary-container": "#4e0011",
                    "secondary": "#fd933d",
                    "secondary-fixed-dim": "#ffb37c",
                    "tertiary-fixed-dim": "#ccd4ee",
                    "primary-fixed": "#ff7481",
                    "on-error": "#490006",
                    "on-surface": "#dbe6fe",
                    "secondary-dim": "#ec8731",
                    "surface-container-lowest": "#000000",
                    "inverse-on-surface": "#4a5569",
                    "error": "#ff716c",
                    "error-dim": "#d7383b",
                    "surface-container-high": "#102036",
                    "surface-variant": "#15263f",
                    "surface-tint": "#ff8c94",
                    "on-tertiary-fixed-variant": "#535b71",
                    "tertiary": "#eef0ff",
                    "on-primary": "#640018",
                    "primary": "#ff8c94",
                    "surface": "#040e1f",
                    "on-primary-fixed": "#000000",
                    "on-background": "#dbe6fe",
                    "on-surface-variant": "#a0abc2",
                    "on-tertiary-container": "#4a5167",
                    "tertiary-container": "#dae2fd",
                    "on-error-container": "#ffa8a3",
                    "surface-container-highest": "#15263f",
                    "primary-container": "#ff7481",
                    "primary-dim": "#e21e49"
            },
            "borderRadius": {
                    "DEFAULT": "0.125rem",
                    "lg": "0.25rem",
                    "xl": "0.5rem",
                    "full": "0.75rem"
            },
            "fontFamily": {
                    "headline": ["Space Grotesk"],
                    "body": ["Manrope"],
                    "label": ["Manrope"]
            }
          },
        },
      }
    </script>
<style>
        .material-symbols-outlined {
            font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
        }
        .hero-gradient {
            background: radial-gradient(circle at 20% 30%, rgba(255, 140, 148, 0.15) 0%, transparent 50%),
                        radial-gradient(circle at 80% 70%, rgba(253, 147, 61, 0.1) 0%, transparent 50%);
        }
        .glass-effect {
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
        }
        .text-glow-primary {
            text-shadow: 0 0 15px rgba(255, 140, 148, 0.4);
        }
        .pattern-grid {
            background-image: radial-gradient(circle, rgba(255, 140, 148, 0.05) 1px, transparent 1px);
            background-size: 24px 24px;
        }
    </style>
</head>
<body class="bg-background text-on-surface font-body selection:bg-primary selection:text-on-primary">
<!-- TopNavBar -->
<nav class="fixed top-0 w-full z-50 bg-surface/60 backdrop-blur-xl border-b border-outline-variant/10">
<div class="flex justify-between items-center px-8 py-4 w-full max-w-screen-2xl mx-auto">
<div class="text-2xl font-black italic tracking-tighter text-primary font-headline">PULSE.AI</div>
<div class="hidden md:flex items-center gap-8">
<a class="text-primary font-bold border-b-2 border-primary pb-1 font-headline tracking-tight transition-all duration-300" href="#">History</a>
<a class="text-on-surface-variant hover:text-primary transition-colors font-headline tracking-tight" href="#">My List</a>
</div>
<div class="flex items-center gap-4">
<button class="hover:opacity-80 transition-all duration-300 scale-95 active:scale-90 transition-transform">
<span class="material-symbols-outlined text-primary">person</span>
</button>
</div>
</div>
</nav>
<main>
<!-- Hero Section -->
<section class="relative min-h-[70vh] flex flex-col items-center justify-center pt-32 px-6 overflow-hidden hero-gradient">
<div class="absolute inset-0 z-0 bg-[url('https://images.unsplash.com/photo-1541562232579-512a21360020?q=80&amp;w=2000')] bg-cover bg-center opacity-10 mix-blend-overlay" data-alt="Dark moody anime aesthetic background"></div>
<div class="relative z-10 w-full max-w-4xl text-center">
<h1 class="text-5xl md:text-8xl font-headline font-bold tracking-tighter mb-6 bg-gradient-to-r from-on-surface via-primary-fixed to-secondary-dim bg-clip-text text-transparent">
                Find Your Next Obsession.
            </h1>
<p class="text-lg md:text-xl text-on-surface-variant max-w-2xl mx-auto mb-12 font-light tracking-wide">
                Describe a vibe, a theme, or an emotion. Our AI does the rest.
            </p>
<!-- Search Interface -->
<div class="relative group max-w-3xl mx-auto mb-8">
<div class="absolute -inset-1 bg-gradient-to-r from-primary via-secondary to-primary rounded-xl blur opacity-20 group-hover:opacity-40 transition duration-1000 group-hover:duration-200"></div>
<div class="relative flex items-center bg-surface-container-highest rounded-xl p-2 shadow-2xl">
<input class="w-full bg-transparent border-none focus:ring-0 px-6 py-4 text-on-surface placeholder:text-on-surface-variant/50 text-lg" placeholder="e.g. A space western with jazz music..." type="text" value="Deep psychological space drama"/>
<button class="bg-gradient-to-b from-primary to-primary-dim text-on-primary px-8 py-4 rounded-lg font-headline font-bold tracking-tight hover:shadow-[0_0_20px_rgba(255,140,148,0.4)] transition-all active:scale-95 whitespace-nowrap">
                        SEARCH
                    </button>
</div>
</div>
<!-- Prompt Pills -->
<div class="flex flex-wrap justify-center gap-3">
<span class="px-5 py-2 rounded-full bg-surface-container-high text-on-surface-variant text-sm font-medium hover:text-secondary hover:bg-surface-container-highest transition-all cursor-pointer border border-outline-variant/10">Gritty space western</span>
<span class="px-5 py-2 rounded-full bg-surface-container-high text-on-surface-variant text-sm font-medium hover:text-secondary hover:bg-surface-container-highest transition-all cursor-pointer border border-outline-variant/10">Magical girl with a dark twist</span>
<span class="px-5 py-2 rounded-full bg-surface-container-high text-on-surface-variant text-sm font-medium hover:text-secondary hover:bg-surface-container-highest transition-all cursor-pointer border border-outline-variant/10">Nostalgic 90s vibes</span>
<span class="px-5 py-2 rounded-full bg-surface-container-high text-on-surface-variant text-sm font-medium hover:text-secondary hover:bg-surface-container-highest transition-all cursor-pointer border border-outline-variant/10">Philosophical AI</span>
</div>
</div>
</section>
<!-- Recommendation Section -->
<section class="py-24 px-8 max-w-screen-2xl mx-auto">
<div class="flex flex-col md:flex-row justify-between items-end mb-16 gap-6">
<div>
<h2 class="text-4xl md:text-5xl font-headline font-bold tracking-tighter mb-4">Top Matches for You</h2>
<p class="text-on-surface-variant font-light text-lg">Curated based on your search for <span class="text-primary font-medium border-b border-primary/30">"Deep psychological space drama"</span></p>
</div>
<div class="flex items-center gap-4 bg-surface-container px-6 py-3 rounded-full border border-outline-variant/20">
<div class="w-12 h-1 bg-primary/20 rounded-full overflow-hidden">
<div class="w-2/3 h-full bg-primary animate-pulse"></div>
</div>
<span class="text-[10px] uppercase tracking-widest text-primary font-black font-headline">AI Scanner Active</span>
</div>
</div>
<div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
<!-- Editorial Card 1: Cowboy Bebop -->
<div class="group relative flex flex-col bg-surface-container-low rounded-2xl overflow-hidden border border-outline-variant/10 hover:border-primary/30 transition-all duration-500 shadow-2xl">
<!-- Background Decoration -->
<div class="absolute top-0 right-0 p-8 opacity-5 pointer-events-none font-headline font-black text-9xl select-none group-hover:opacity-10 transition-opacity">01</div>
<div class="absolute inset-0 pattern-grid opacity-20 pointer-events-none"></div>
<div class="p-10 relative flex flex-col h-full z-10">
<div class="flex justify-between items-start mb-6">
<div class="px-3 py-1 bg-secondary/10 border border-secondary/20 rounded-md">
<span class="text-[11px] font-black text-secondary uppercase tracking-widest font-headline">Score: 8.75 / 10</span>
</div>
<span class="material-symbols-outlined text-outline-variant group-hover:text-primary transition-colors">rocket_launch</span>
</div>
<h3 class="text-3xl font-headline font-bold mb-6 tracking-tight group-hover:text-primary transition-colors">Cowboy Bebop</h3>
<div class="flex flex-wrap gap-2 mb-8">
<span class="text-[10px] px-2 py-1 rounded bg-surface-container-highest text-on-surface-variant font-bold uppercase tracking-tighter">Action</span>
<span class="text-[10px] px-2 py-1 rounded bg-surface-container-highest text-on-surface-variant font-bold uppercase tracking-tighter">Sci-Fi</span>
<span class="text-[10px] px-2 py-1 rounded bg-surface-container-highest text-on-surface-variant font-bold uppercase tracking-tighter">Space Western</span>
</div>
<div class="relative mb-10 group/text">
<div class="max-h-48 overflow-y-auto pr-4 text-on-surface-variant text-sm leading-relaxed scrollbar-thin scrollbar-thumb-primary/20">
                            Crime is timeless. In the year 2071, humanity has expanded across the galaxy, filling the surface of planets and moons with settlements like those on Earth. These new frontiers are regulated by the Inter Solar System Police, who are kept in check by bounty hunters known as "Cowboys." Spike Spiegel and Jet Black pursue criminals throughout the solar system to make a living. However, Spike is haunted by the weight of his past. As the crew of the Bebop grows, the mystery of Spike's past is slowly revealed.
                        </div>
<div class="absolute bottom-0 left-0 right-0 h-12 bg-gradient-to-t from-surface-container-low to-transparent pointer-events-none"></div>
</div>
<div class="mt-auto pt-8 border-t border-outline-variant/10">
<div class="flex items-center gap-3 mb-3">
<span class="material-symbols-outlined text-primary text-sm">psychology</span>
<p class="text-[10px] text-primary font-black uppercase tracking-[0.2em] font-headline">AI Insight</p>
</div>
<p class="text-xs text-on-surface-variant italic leading-snug">
                            Matches your preference for <span class="text-on-surface font-semibold">existential themes</span> and <span class="text-on-surface font-semibold">cinematic atmosphere</span>.
                        </p>
</div>
</div>
</div>
<!-- Editorial Card 2: Cowboy Bebop Movie -->
<div class="group relative flex flex-col bg-surface-container-low rounded-2xl overflow-hidden border border-outline-variant/10 hover:border-secondary/30 transition-all duration-500 shadow-2xl">
<!-- Background Decoration -->
<div class="absolute top-0 right-0 p-8 opacity-5 pointer-events-none font-headline font-black text-9xl select-none group-hover:opacity-10 transition-opacity">05</div>
<div class="absolute inset-0 pattern-grid opacity-20 pointer-events-none"></div>
<div class="p-10 relative flex flex-col h-full z-10">
<div class="flex justify-between items-start mb-6">
<div class="px-3 py-1 bg-primary/10 border border-primary/20 rounded-md">
<span class="text-[11px] font-black text-primary uppercase tracking-widest font-headline">Score: 8.38 / 10</span>
</div>
<span class="material-symbols-outlined text-outline-variant group-hover:text-secondary transition-colors">movie</span>
</div>
<h3 class="text-3xl font-headline font-bold mb-6 tracking-tight group-hover:text-secondary transition-colors">Tengoku no Tobira</h3>
<div class="flex flex-wrap gap-2 mb-8">
<span class="text-[10px] px-2 py-1 rounded bg-surface-container-highest text-on-surface-variant font-bold uppercase tracking-tighter">Action</span>
<span class="text-[10px] px-2 py-1 rounded bg-surface-container-highest text-on-surface-variant font-bold uppercase tracking-tighter">Drama</span>
<span class="text-[10px] px-2 py-1 rounded bg-surface-container-highest text-on-surface-variant font-bold uppercase tracking-tighter">Psychological</span>
</div>
<div class="relative mb-10 group/text">
<div class="max-h-48 overflow-y-auto pr-4 text-on-surface-variant text-sm leading-relaxed">
                            A countdown to destruction begins in the days leading up to Halloween 2071. A terrorist explosion on Mars releases a deadly pathogen, and a massive bounty is placed on the perpetrator. The Bebop crew takes the case, leading Spike into a confrontation with a man whose past is as mysterious as his own, challenging Spike’s concepts of reality and dreams.
                        </div>
<div class="absolute bottom-0 left-0 right-0 h-12 bg-gradient-to-t from-surface-container-low to-transparent pointer-events-none"></div>
</div>
<div class="mt-auto pt-8 border-t border-outline-variant/10">
<div class="flex items-center gap-3 mb-3">
<span class="material-symbols-outlined text-secondary text-sm">bolt</span>
<p class="text-[10px] text-secondary font-black uppercase tracking-[0.2em] font-headline">AI Insight</p>
</div>
<p class="text-xs text-on-surface-variant italic leading-snug">
                            Recommended for its <span class="text-on-surface font-semibold">gritty urban aesthetic</span> and <span class="text-on-surface font-semibold">philosophical stakes</span>.
                        </p>
</div>
</div>
</div>
<!-- Editorial Card 3: Trigun -->
<div class="group relative flex flex-col bg-surface-container-low rounded-2xl overflow-hidden border border-outline-variant/10 hover:border-primary/30 transition-all duration-500 shadow-2xl">
<!-- Background Decoration -->
<div class="absolute top-0 right-0 p-8 opacity-5 pointer-events-none font-headline font-black text-9xl select-none group-hover:opacity-10 transition-opacity">06</div>
<div class="absolute inset-0 pattern-grid opacity-20 pointer-events-none"></div>
<div class="p-10 relative flex flex-col h-full z-10">
<div class="flex justify-between items-start mb-6">
<div class="px-3 py-1 bg-secondary/10 border border-secondary/20 rounded-md">
<span class="text-[11px] font-black text-secondary uppercase tracking-widest font-headline">Score: 8.21 / 10</span>
</div>
<span class="material-symbols-outlined text-outline-variant group-hover:text-primary transition-colors">adjust</span>
</div>
<h3 class="text-3xl font-headline font-bold mb-6 tracking-tight group-hover:text-primary transition-colors">Trigun</h3>
<div class="flex flex-wrap gap-2 mb-8">
<span class="text-[10px] px-2 py-1 rounded bg-surface-container-highest text-on-surface-variant font-bold uppercase tracking-tighter">Adventure</span>
<span class="text-[10px] px-2 py-1 rounded bg-surface-container-highest text-on-surface-variant font-bold uppercase tracking-tighter">Comedy</span>
<span class="text-[10px] px-2 py-1 rounded bg-surface-container-highest text-on-surface-variant font-bold uppercase tracking-tighter">Sci-Fi</span>
</div>
<div class="relative mb-10 group/text">
<div class="max-h-48 overflow-y-auto pr-4 text-on-surface-variant text-sm leading-relaxed">
                            Vash the Stampede is a man with a $$60,000,000,000 bounty on his head. The reason? He's a merciless villain who lays waste to all those that oppose him and flattens entire cities for fun. Or so the rumors say. In reality, Vash is a softhearted pacifist who is actually a skilled gunslinger. He travels the desert planet Gunsmoke while being followed by two insurance agents who try to minimize the damage caused by his presence.
                        </div>
<div class="absolute bottom-0 left-0 right-0 h-12 bg-gradient-to-t from-surface-container-low to-transparent pointer-events-none"></div>
</div>
<div class="mt-auto pt-8 border-t border-outline-variant/10">
<div class="flex items-center gap-3 mb-3">
<span class="material-symbols-outlined text-primary text-sm">flare</span>
<p class="text-[10px] text-primary font-black uppercase tracking-[0.2em] font-headline">AI Insight</p>
</div>
<p class="text-xs text-on-surface-variant italic leading-snug">
                            Perfect balance of <span class="text-on-surface font-semibold">character mystery</span> and <span class="text-on-surface font-semibold">post-apocalyptic world-building</span>.
                        </p>
</div>
</div>
</div>
</div>
</section>
</main>
<!-- Footer -->
<footer class="bg-surface-container-lowest dark:bg-surface-container-lowest w-full py-16 px-8 border-t border-outline-variant/10">
<div class="flex flex-col md:flex-row justify-between items-center gap-10 w-full max-w-screen-2xl mx-auto">
<div class="font-headline font-black text-primary tracking-tighter text-2xl italic">PULSE.AI</div>
<div class="flex gap-12">
<a class="font-body text-[10px] tracking-[0.2em] uppercase text-on-surface-variant hover:text-primary transition-colors duration-300" href="#">Privacy Policy</a>
<a class="font-body text-[10px] tracking-[0.2em] uppercase text-on-surface-variant hover:text-primary transition-colors duration-300" href="#">Terms of Service</a>
<a class="font-body text-[10px] tracking-[0.2em] uppercase text-on-surface-variant hover:text-primary transition-colors duration-300" href="#">API Docs</a>
</div>
<div class="font-headline text-[10px] tracking-widest uppercase text-secondary/60">
            © 2024 CINEMATIC PULSE AI. <span class="text-outline">SYSTEM_STABLE_V.4.2</span>
</div>
</div>
</footer>
</body></html>

custom_exception.py: 
import sys

class CustomException(Exception):
    def __init__ (self, message:str, error_detail: Exception = None):
        self.error_message = self.get_detailed_error_message(message, error_detail)
        super().__init__(self.error_message)

@staticmethod
def get_detailed_error_message(message, error_detail):
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown File"
    line_number = exc_tb.tb_lineno if exc_tb else "Unknown Line" 
    return f"{message} | Error: {error_detail} | File:{file_name} | Line:{line_number}"

def __str__(self):
    return self.error_message

logger.py: 
import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOGS_DIR, f"log_{datetime.now().strftime('%Y-%m-%d')}.log")

logging.basicConfig(
    filename=LOG_FILE,
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger

api.py:

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from pipeline.pipeline import AnimeRecommendationPipeline

app = FastAPI(title="Anime Recommender")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

pipeline = AnimeRecommendationPipeline()


class RecommendationRequest(BaseModel):
    query: str


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/recommend")
def recommend(data: RecommendationRequest):
    result = pipeline.recommend(data.query)
    return {
        "query": data.query,
        "recommendation": result
    }

setup.py: 

from setuptools import setup, find_packages

with open ("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ANIME-RECOMMENDER",
    version="0.1",
    author="Eduardo Sousa",
    packages=find_packages(),
    install_requires = requirements,

)

requirements.txt: 

aiohappyeyeballs==2.6.1
aiohttp==3.13.3
aiosignal==1.4.0
altair==6.0.0
# Editable install with no version control (ANIME-RECOMMENDER==0.1)
-e c:\users\z004hn4c\documents\estudo\llmops and aiops bootcamp with 8 end to end projects\anime_recomender_project
annotated-doc==0.0.4
annotated-types==0.7.0
anyio==4.12.1
attrs==25.4.0
bcrypt==5.0.0
blinker==1.9.0
build==1.4.0
cachetools==7.0.5
certifi==2026.2.25
charset-normalizer==3.4.6
chromadb==1.5.5
click==8.3.1
colorama==0.4.6
dataclasses-json==0.6.7
distro==1.9.0
durationpy==0.10
fastapi==0.135.3
filelock==3.25.2
flatbuffers==25.12.19
frozenlist==1.8.0
fsspec==2026.2.0
gitdb==4.0.12
GitPython==3.1.46
googleapis-common-protos==1.73.0
greenlet==3.3.2
groq==0.37.1
grpcio==1.78.0
h11==0.16.0
hf-xet==1.4.2
httpcore==1.0.9
httptools==0.7.1
httpx==0.28.1
httpx-sse==0.4.3
huggingface_hub==1.7.1
idna==3.11
importlib_metadata==8.7.1
importlib_resources==6.5.2
Jinja2==3.1.6
joblib==1.5.3
jsonpatch==1.33
jsonpointer==3.0.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
kubernetes==35.0.0
langchain==1.2.12
langchain-classic==1.0.3
langchain-community==0.4.1
langchain-core==1.2.19
langchain-groq==1.1.2
langchain-huggingface==1.2.1
langchain-text-splitters==1.1.1
langgraph==1.1.2
langgraph-checkpoint==4.0.1
langgraph-prebuilt==1.0.8
langgraph-sdk==0.3.11
langsmith==0.7.20
markdown-it-py==4.0.0
MarkupSafe==3.0.3
marshmallow==3.26.2
mdurl==0.1.2
mmh3==5.2.1
mpmath==1.3.0
multidict==6.7.1
mypy_extensions==1.1.0
narwhals==2.18.0
networkx==3.6.1
numpy==2.4.3
oauthlib==3.3.1
onnxruntime==1.24.4
opentelemetry-api==1.40.0
opentelemetry-exporter-otlp-proto-common==1.40.0
opentelemetry-exporter-otlp-proto-grpc==1.40.0
opentelemetry-proto==1.40.0
opentelemetry-sdk==1.40.0
opentelemetry-semantic-conventions==0.61b0
orjson==3.11.7
ormsgpack==1.12.2
overrides==7.7.0
packaging==26.0
pandas==2.3.3
pillow==12.1.1
propcache==0.4.1
protobuf==6.33.5
pyarrow==23.0.1
pybase64==1.4.3
pydantic==2.12.5
pydantic-settings==2.13.1
pydantic_core==2.41.5
pydeck==0.9.1
Pygments==2.19.2
PyPika==0.51.1
pyproject_hooks==1.2.0
python-dateutil==2.9.0.post0
python-dotenv==1.2.2
python-multipart==0.0.26
pytz==2026.1.post1
PyYAML==6.0.3
referencing==0.37.0
regex==2026.2.28
requests==2.32.5
requests-oauthlib==2.0.0
requests-toolbelt==1.0.0
rich==14.3.3
rpds-py==0.30.0
safetensors==0.7.0
scikit-learn==1.8.0
scipy==1.17.1
sentence-transformers==5.3.0
setuptools==82.0.1
shellingham==1.5.4
six==1.17.0
smmap==5.0.3
sniffio==1.3.1
SQLAlchemy==2.0.48
starlette==1.0.0
streamlit==1.55.0
sympy==1.14.0
tenacity==9.1.4
threadpoolctl==3.6.0
tokenizers==0.22.2
toml==0.10.2
torch==2.10.0
tornado==6.5.5
tqdm==4.67.3
transformers==5.3.0
typer==0.24.1
typing-inspect==0.9.0
typing-inspection==0.4.2
typing_extensions==4.15.0
tzdata==2025.3
urllib3==2.6.3
uuid_utils==0.14.1
uvicorn==0.42.0
watchdog==6.0.0
watchfiles==1.1.1
websocket-client==1.9.0
websockets==16.0
xxhash==3.6.0
yarl==1.23.0
zipp==3.23.0
zstandard==0.25.0
