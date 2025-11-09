function showInteractiveDoc() {
    const btn = event.target.closest('.btn-interactive');
    const originalHTML = btn.innerHTML;

    btn.innerHTML = '<iconify-icon icon="mdi:loading" class="spin-icon"></iconify-icon><span>Loading...</span>';
    btn.disabled = true;

    setTimeout(() => {
        const interactiveWindow = window.open('', 'Interactive Document', 'width=1200,height=800');
        interactiveWindow.document.write(`<!DOCTYPE html><html><head><title>Interactive Document - Zan-AI</title><style>*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Inter',sans-serif;background:linear-gradient(135deg,#EBF4FF 0%,#f5f0ff 100%);padding:40px 20px}.container{max-width:1000px;margin:0 auto;background:white;border-radius:16px;padding:40px;box-shadow:0 10px 40px rgba(0,0,0,0.1)}h1{background:linear-gradient(90deg,#3C55E6 0%,#E20262 50%,#FF7401 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:30px}button{background:linear-gradient(90deg,#FF7401 0%,#E20262 100%);color:white;border:none;padding:10px 20px;border-radius:8px;cursor:pointer;margin:10px 5px;font-weight:600}</style></head><body><div class="container"><h1>📊 Interactive Analysis Dashboard</h1><p>Your research has been thoroughly analyzed.</p><button onclick="window.print()">🖨️ Print</button><button onclick="window.close()">❌ Close</button></div></body></html>`);
        interactiveWindow.document.close();

        btn.innerHTML = originalHTML;
        btn.disabled = false;
    }, 2000);
}