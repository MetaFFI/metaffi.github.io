const codeBlock = document.getElementById('code-block');
const languageSelector = document.getElementById('language-selector');

// Update code block based on selected language
languageSelector.addEventListener('change', async () => {
    const selectedLanguage = languageSelector.value;
    try {
        let filename;
        switch (selectedLanguage) {
            case 'python':
                filename = 'log4j.py';
                break;
            case 'go':
                filename = 'log4j.go';
                break;
            default:
                console.error('Invalid language selection');
                return;
        }

        const response = await fetch(filename);
        const codeSnippet = await response.text();
        codeBlock.textContent = codeSnippet;
        codeBlock.className = `language-${selectedLanguage}`;
        Prism.highlightElement(codeBlock); // Apply syntax highlighting
    } catch (error) {
        console.error('Error loading code:', error);
    }
});

// Initialize with Python code
languageSelector.value = 'python';
languageSelector.dispatchEvent(new Event('change')); // Trigger initial load