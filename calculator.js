let memoryValue = 0;

function insertText(text) {
    const display = document.getElementById('display');
    display.value += text;
}

function clearDisplay() {
    document.getElementById('display').value = '';
}

function backspace() {
    const display = document.getElementById('display');
    display.value = display.value.slice(0, -1);
}

async function handleOperation(operation) {
    const display = document.getElementById('display');
    const value = display.value;

    if (value === '' && operation !== 'calculate') {
        alert('Please enter a valid number');
        return;
    }

    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                operation: operation,
                value: value
            })
        });

        const data = await response.json();
        if (data.success) {
            display.value = data.result;
        } else {
            alert(data.error);
        }
    } catch (error) {
        alert('An error occurred');
        console.error(error);
    }
}

async function calculate() {
    const display = document.getElementById('display');
    const expression = display.value;

    if (expression === '') {
        return;
    }

    try {
        const response = await fetch('/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                operation: 'calculate',
                expression: expression
            })
        });

        const data = await response.json();
        if (data.success) {
            display.value = data.result;
        } else {
            alert(data.error);
        }
    } catch (error) {
        alert('An error occurred');
        console.error(error);
    }
}

async function clearHistory() {
    try {
        await fetch('/clear_history', {
            method: 'POST'
        });
        updateHistoryDisplay();
    } catch (error) {
        alert('Failed to clear history');
        console.error(error);
    }
}

async function updateHistoryDisplay() {
    try {
        const response = await fetch('/get_history');
        const data = await response.json();
        const historyContent = document.getElementById('historyContent');
        historyContent.innerHTML = '';
        
        data.history.forEach((item) => {
            const historyItem = document.createElement('div');
            historyItem.className = 'history-item';
            historyItem.innerHTML = item;
            historyItem.onclick = function() {
                const parts = item.split(' = ');
                document.getElementById('display').value = parts[1];
            };
            historyContent.appendChild(historyItem);
        });
    } catch (error) {
        console.error('Error fetching history:', error);
    }
}

function toggleHistory() {
    const historyDiv = document.getElementById('history');
    if (historyDiv.style.display === 'none' || historyDiv.style.display === '') {
        historyDiv.style.display = 'block';
        updateHistoryDisplay();
    } else {
        historyDiv.style.display = 'none';
    }
}

function memory(operation) {
    const display = document.getElementById('display');
    const value = parseFloat(display.value);
    
    if (operation === 'MS') {
        if (!isNaN(value)) {
            memoryValue = value;
            alert('Value stored in memory');
        }
    } else if (operation === 'MR') {
        display.value = memoryValue;
    }
}

function showAbout() {
    alert('Scientific Calculator\nVersion 2.0\n\nEnhanced with Python backend and history functions');
}

// Handle keyboard input
document.addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        calculate();
    } else if (event.key === 'Backspace') {
        backspace();
    } else if (/[\d+\-*/.,()^]/.test(event.key)) {
        insertText(event.key);
    }
});

// Initialize
document.getElementById('historyButton').addEventListener('click', toggleHistory);