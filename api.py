from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import logging
import sys
import os

# Adicionar o diretório atual ao PATH
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Importar o pipeline
try:
    from pipeline.pipeline import AnimeRecommendationPipeline
    logger.info("Pipeline importado com sucesso")
except Exception as e:
    logger.error(f"Erro ao importar pipeline: {str(e)}")
    raise

app = FastAPI(title="Anime Recommender API")

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Criar diretórios se não existirem
os.makedirs("static", exist_ok=True)
os.makedirs("templates", exist_ok=True)
os.makedirs("static/js", exist_ok=True)

# Montar arquivos estáticos
app.mount("/static", StaticFiles(directory="static"), name="static")

# Inicializar o pipeline (cacheado)
_pipeline = None

def get_pipeline():
    global _pipeline
    if _pipeline is None:
        logger.info("Initializing Anime Recommendation Pipeline...")
        try:
            _pipeline = AnimeRecommendationPipeline()
            logger.info("Pipeline initialized successfully!")
        except Exception as e:
            logger.error(f"Failed to initialize pipeline: {str(e)}")
            raise
    return _pipeline

class RecommendationRequest(BaseModel):
    query: str

class RecommendationResponse(BaseModel):
    success: bool
    query: str
    recommendation: str
    error: Optional[str] = None

# Função para ler o arquivo HTML
def get_html_content():
    html_path = os.path.join("templates", "index.html")
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error reading HTML file: {str(e)}")
        return None

@app.get("/", response_class=HTMLResponse)
async def home():
    """Serve a página principal"""
    try:
        html_content = get_html_content()
        
        if html_content is None:
            # HTML alternativo embutido
            return HTMLResponse(content="""
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Anime Recommender</title>
                <script src="https://cdn.tailwindcss.com"></script>
                <style>
                    .loading {
                        display: none;
                        position: fixed;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        background: rgba(0,0,0,0.8);
                        padding: 20px;
                        border-radius: 10px;
                        z-index: 1000;
                    }
                </style>
            </head>
            <body class="bg-gray-900 text-white">
                <div class="loading" id="loading">
                    <div class="text-center">
                        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-pink-500 mx-auto mb-4"></div>
                        <p>Gerando recomendações...</p>
                    </div>
                </div>
                
                <div class="container mx-auto px-4 py-8">
                    <h1 class="text-5xl font-bold text-center mb-4 bg-gradient-to-r from-pink-500 to-orange-500 bg-clip-text text-transparent">
                        Anime Recommender System
                    </h1>
                    <p class="text-center text-gray-400 mb-8">Find your next anime based on your preferences</p>
                    
                    <div class="max-w-2xl mx-auto">
                        <div class="mb-4">
                            <input type="text" id="searchInput" 
                                   class="w-full px-6 py-3 bg-gray-800 border border-gray-700 rounded-lg focus:outline-none focus:border-pink-500 text-lg"
                                   placeholder="Describe what anime you want to watch...">
                        </div>
                        <button id="searchBtn" 
                                class="w-full bg-gradient-to-r from-pink-600 to-orange-600 hover:from-pink-700 hover:to-orange-700 text-white font-bold py-3 px-4 rounded-lg transition transform hover:scale-105">
                            Search
                        </button>
                    </div>
                    
                    <div id="results" class="mt-12 max-w-4xl mx-auto"></div>
                </div>
                
                <script>
                    const searchBtn = document.getElementById('searchBtn');
                    const searchInput = document.getElementById('searchInput');
                    const resultsDiv = document.getElementById('results');
                    const loadingDiv = document.getElementById('loading');
                    
                    async function getRecommendations() {
                        const query = searchInput.value.trim();
                        if (!query) return;
                        
                        // Mostrar loading
                        loadingDiv.style.display = 'block';
                        resultsDiv.innerHTML = '';
                        
                        try {
                            const response = await fetch('/api/recommend', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json',
                                },
                                body: JSON.stringify({ query: query })
                            });
                            
                            const data = await response.json();
                            
                            if (data.success) {
                                // Formatar a resposta
                                const formattedText = data.recommendation
                                    .replace(/\\n/g, '<br>')
                                    .replace(/\\*\\*(.*?)\\*\\*/g, '<strong>$1</strong>')
                                    .replace(/\\*(.*?)\\*/g, '<em>$1</em>');
                                
                                resultsDiv.innerHTML = `
                                    <div class="bg-gray-800 rounded-xl p-8 shadow-2xl">
                                        <h2 class="text-2xl font-bold mb-2 text-pink-400">Recommendations</h2>
                                        <p class="text-gray-400 mb-6">Based on: "${escapeHtml(data.query)}"</p>
                                        <div class="prose prose-invert max-w-none">
                                            ${formattedText}
                                        </div>
                                    </div>
                                `;
                            } else {
                                resultsDiv.innerHTML = `
                                    <div class="bg-red-900/50 border-2 border-red-500 rounded-lg p-6">
                                        <h3 class="text-red-400 font-bold mb-2">Error</h3>
                                        <p class="text-red-300">${escapeHtml(data.error)}</p>
                                    </div>
                                `;
                            }
                        } catch (error) {
                            resultsDiv.innerHTML = `
                                <div class="bg-red-900/50 border-2 border-red-500 rounded-lg p-6">
                                    <h3 class="text-red-400 font-bold mb-2">Connection Error</h3>
                                    <p class="text-red-300">${escapeHtml(error.message)}</p>
                                    <p class="text-gray-400 mt-2">Make sure the server is running.</p>
                                </div>
                            `;
                        } finally {
                            // Esconder loading
                            loadingDiv.style.display = 'none';
                        }
                    }
                    
                    function escapeHtml(text) {
                        const div = document.createElement('div');
                        div.textContent = text;
                        return div.innerHTML;
                    }
                    
                    searchBtn.addEventListener('click', getRecommendations);
                    searchInput.addEventListener('keypress', (e) => {
                        if (e.key === 'Enter') {
                            getRecommendations();
                        }
                    });
                    
                    // Adicionar estilos extras
                    const style = document.createElement('style');
                    style.textContent = `
                        .prose {
                            line-height: 1.6;
                        }
                        .prose strong {
                            color: #f472b6;
                        }
                        .prose p {
                            margin-bottom: 1rem;
                        }
                    `;
                    document.head.appendChild(style);
                </script>
            </body>
            </html>
            """)
        
        return HTMLResponse(content=html_content)
        
    except Exception as e:
        logger.error(f"Error loading page: {str(e)}", exc_info=True)
        return HTMLResponse(content=f"""
        <html>
            <body style="font-family: Arial; padding: 20px;">
                <h1>Error</h1>
                <p>{str(e)}</p>
            </body>
        </html>
        """, status_code=500)

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "Anime Recommender"}

@app.post("/api/recommend", response_model=RecommendationResponse)
async def get_recommendation(request: RecommendationRequest):
    """
    Endpoint para obter recomendações de anime baseadas na query do usuário
    """
    try:
        logger.info(f"Received recommendation request: {request.query}")
        
        # Obter o pipeline e fazer a recomendação
        pipeline = get_pipeline()
        recommendation = pipeline.recommend(request.query)
        
        logger.info(f"Recommendation generated successfully for query: {request.query}")
        
        return RecommendationResponse(
            success=True,
            query=request.query,
            recommendation=recommendation,
            error=None
        )
        
    except Exception as e:
        logger.error(f"Error generating recommendation: {str(e)}", exc_info=True)
        return RecommendationResponse(
            success=False,
            query=request.query,
            recommendation="",
            error=f"Desculpe, ocorreu um erro ao gerar as recomendações: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    print("=" * 50)
    print("🎬 Anime Recommender System - API Server")
    print("=" * 50)
    print(f"📁 Diretório atual: {os.getcwd()}")
    print(f"📄 Index.html existe? {os.path.exists('templates/index.html')}")
    print("=" * 50)
    print("🚀 Servidor rodando em: http://localhost:8000")
    print("📝 Documentação: http://localhost:8000/docs")
    print("=" * 50)
    
    # Executar o servidor
    uvicorn.run(
        "api:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )