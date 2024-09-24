const codeBlock = document.getElementById('code-block');
const languageSelector = document.getElementById('language-selector');

// Update code block based on selected language
languageSelector.addEventListener('change', () => {
    const selectedLanguage = languageSelector.value;
    if (selectedLanguage === 'python') {
        codeBlock.textContent = `# Python code to call log4j\nimport logging\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\nlogger.info("This is a log message from Python")`;
        codeBlock.className = 'language-python'; // Add the language class
    } else if (selectedLanguage === 'go') {
        codeBlock.textContent = `// Go code to call log4j\npackage main\nimport (\n\t"fmt"\n\t"github.com/sirupsen/logrus"\n)\nfunc main() {\n\tlogrus.Info("This is a log message from Go")\n}`;
        codeBlock.className = 'language-go'; // Add the language class
    }
    Prism.highlightElement(codeBlock); // Apply syntax highlighting
});

// Initialize with Python code
languageSelector.value = 'python';
codeBlock.textContent = `# Python code to call log4j\nimport logging\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\nlogger.info("This is a log message from Python")`;
codeBlock.className = 'language-python'; // Initialize with the language class
Prism.highlightElement(codeBlock); // Apply syntax highlighting initially
