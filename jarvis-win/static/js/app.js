async function testAPI() {
    const response = await fetch('/api/test');

    const data = await response.json();

    document.getElementById('result').innerText = data.message;
}