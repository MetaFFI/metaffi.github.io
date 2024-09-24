const codeBlock = document.getElementById('code-block');
const languageTabs = document.querySelectorAll('.language-tabs button');

// Handle tab click
languageTabs.forEach(tab => {
    tab.addEventListener('click', () => {
        const selectedLanguage = tab.getAttribute('data-language');
        loadCodeSnippet(selectedLanguage);

        // Update active tab styling
        languageTabs.forEach(t => {
            if (t === tab) {
                t.classList.add('active-tab'); // Set the clicked tab as active
            } else {
                t.classList.remove('active-tab'); // Remove active class from other tabs
                t.style.backgroundColor = '#f0f0f0';
            }
        });
    });

    // Add hover effect
    tab.addEventListener('mouseenter', () => {
        tab.style.backgroundColor = '#a4a4a4';
    });

    tab.addEventListener('mouseleave', () => {
        // Only change background color if not active
        if (!tab.classList.contains('active-tab')) {
            tab.style.backgroundColor = '#f0f0f0';
        }
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