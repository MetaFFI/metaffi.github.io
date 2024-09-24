# Log4j Examples

Choose a language:
<select id="language-selector">
    <option value="python">Python</option>
    <option value="go">Go</option>
</select>

<pre><code id="code-block"></code></pre>

<script>
    const codeBlock = document.getElementById('code-block');
    const languageSelector = document.getElementById('language-selector');

    // Update code block based on selected language
    languageSelector.addEventListener('change', () => {
        const selectedLanguage = languageSelector.value;
        if (selectedLanguage === 'python') {
            codeBlock.textContent = `# Python code to call log4j\nimport logging\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\nlogger.info("This is a log message from Python")`;
        } else if (selectedLanguage === 'go') {
            codeBlock.textContent = `// Go code to call log4j\npackage main\nimport (\n\t\"fmt\"\n\t\"github.com/sirupsen/logrus\"\n)\nfunc main() {\n\tlogrus.Info(\"This is a log message from Go\")\n}`;
        }
    });

    // Initialize with Python code
    languageSelector.value = 'python';
    codeBlock.textContent = `# Python code to call log4j\nimport logging\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\nlogger.info("This is a log message from Python")`;
</script>
