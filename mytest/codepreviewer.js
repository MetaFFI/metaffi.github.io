const codeBlock = document.getElementById('code-block');
const languageTabs = document.querySelectorAll('.language-tabs button');

// Handle tab click
languageTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const selectedLanguage = tab.getAttribute('data-language');
        loadCodeSnippet(selectedLanguage);
        // Update active tab styling
        languageTabs.forEach(t => t.classList.remove('active-tab'));
        tab.classList.add('active-tab');
    });
});

// Load code snippet based on selected language
async function loadCodeSnippet(language) {
    try {
        const response = await fetch(getFilename(language));
        const codeSnippet = await response.text();
        codeBlock.textContent = codeSnippet;
        codeBlock.className = `language-${language}`;
        Prism.highlightElement(codeBlock); // Apply syntax highlighting
    } catch (error) {
        console.error('Error loading code:', error);
    }
}

// Initialize with Python code
loadCodeSnippet('python');

// Map language to filename
function getFilename(language) {
    switch (language) {
        case 'python':
            return 'log4j.py';
        case 'go':
            return 'log4j.go';
        default:
            return '';
    }
}