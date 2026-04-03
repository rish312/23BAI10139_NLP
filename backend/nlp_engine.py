import logging
from transformers import pipeline

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NLPEngine:
    def __init__(self):
        logger.info("Initializing NLP models... This may take a moment.")
        try:
            # Explicitly load light weight models to save memory and speed up initial load
            self.summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
            self.sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
            logger.info("NLP models loaded successfully.")
        except Exception as e:
            logger.error(f"Failed to load NLP models: {e}")
            raise e

    def summarize_text(self, text: str) -> str:
        """
        Summarize the given text.
        """
        if not text or len(text.strip()) == 0:
            return ""
        
        try:
            # Max length cannot exceed the input text length reasonably, adding safety checks
            input_length = len(text.split())
            max_len = min(130, max(30, int(input_length * 0.6)))
            min_len = min(30, max(10, int(input_length * 0.2)))
            
            result = self.summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
            return result[0]['summary_text']
        except Exception as e:
            logger.error(f"Summarization error: {e}")
            return f"Error during summarization: {str(e)}"

    def analyze_sentiment(self, text: str) -> dict:
        """
        Analyze the sentiment of the given text.
        Returns a dict with 'label' and 'score'.
        """
        if not text or len(text.strip()) == 0:
            return {"label": "NEUTRAL", "score": 0.0}
        
        try:
            # Predict
            result = self.sentiment_analyzer(text)[0]
            return {
                "label": result['label'],
                "score": result['score']
            }
        except Exception as e:
            logger.error(f"Sentiment analysis error: {e}")
            return {"label": "ERROR", "score": 0.0}

# Global singleton instance of the engine
# This avoids reloading the model on every request
engine = None

def get_engine():
    global engine
    if engine is None:
        engine = NLPEngine()
    return engine
