document.addEventListener('DOMContentLoaded', () => {
    const textInput = document.getElementById('text-input');
    const analyzeBtn = document.getElementById('btn-analyze');
    const btnText = analyzeBtn.querySelector('.btn-text');
    const loader = analyzeBtn.querySelector('.loader');
    
    const resultsSection = document.getElementById('results-section');
    const sentimentEmoji = document.getElementById('sentiment-emoji');
    const sentimentLabel = document.getElementById('sentiment-label');
    const scoreBar = document.getElementById('score-bar');
    const summaryText = document.getElementById('summary-text');

    const sentimentConfig = {
        'POSITIVE': { color: 'var(--positive)', emoji: '✨' },
        'NEGATIVE': { color: 'var(--negative)', emoji: '💔' },
        'NEUTRAL': { color: 'var(--neutral)', emoji: '😐' },
        'ERROR': { color: 'var(--text-secondary)', emoji: '⚠️' }
    };

    analyzeBtn.addEventListener('click', async () => {
        const text = textInput.value.trim();
        if (!text) {
            alert("Please enter some text to analyze.");
            return;
        }

        // UI Loading State
        analyzeBtn.disabled = true;
        btnText.textContent = "Analyzing...";
        loader.classList.remove('hidden');
        resultsSection.classList.add('hidden');

        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text })
            });

            if (!response.ok) {
                throw new Error("Server returned an error");
            }

            const data = await response.json();
            
            // Populate Summary
            summaryText.textContent = data.summary;

            // Populate Sentiment
            const labelStr = data.sentiment.label.toUpperCase();
            const config = sentimentConfig[labelStr] || sentimentConfig['NEUTRAL'];
            const roundedScore = Math.round(data.sentiment.score * 100);
            
            sentimentEmoji.textContent = config.emoji;
            sentimentLabel.textContent = `${labelStr} (${roundedScore}%)`;
            sentimentLabel.style.color = config.color;
            
            scoreBar.style.backgroundColor = config.color;
            // Delay the width change slightly to trigger CSS transition nicely
            setTimeout(() => {
                scoreBar.style.width = `${roundedScore}%`;
            }, 100);

            // Show results
            resultsSection.classList.remove('hidden');

        } catch (error) {
            console.error(error);
            alert("An error occurred during analysis. Please try again.");
        } finally {
            // UI Reset State
            analyzeBtn.disabled = false;
            btnText.textContent = "Analyze Insights";
            loader.classList.add('hidden');
        }
    });
});
