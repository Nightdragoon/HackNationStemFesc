function showInteractiveDoc() {
    const btn = event.target.closest('.btn-interactive');
    const originalHTML = btn.innerHTML;

    btn.innerHTML = '<iconify-icon icon="mdi:loading" class="spin-icon"></iconify-icon><span>Loading...</span>';
    btn.disabled = true;

    // Simular carga del documento interactivo
    setTimeout(() => {
        const interactiveWindow = window.open('', 'Interactive Document', 'width=1200,height=800');

        interactiveWindow.document.write(`
                    <!DOCTYPE html>
                    <html>
                    <head>
                        <title>Interactive Document - Zan-AI</title>
                        <style>
                            * {
                                margin: 0;
                                padding: 0;
                                box-sizing: border-box;
                            }
                            body {
                                font-family: 'Inter', sans-serif;
                                background: linear-gradient(135deg, #EBF4FF 0%, #f5f0ff 100%);
                                padding: 40px 20px;
                            }
                            .container {
                                max-width: 1000px;
                                margin: 0 auto;
                                background: white;
                                border-radius: 16px;
                                padding: 40px;
                                box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
                            }
                            h1 {
                                background: linear-gradient(90deg, #3C55E6 0%, #E20262 50%, #FF7401 100%);
                                -webkit-background-clip: text;
                                -webkit-text-fill-color: transparent;
                                background-clip: text;
                                margin-bottom: 30px;
                            }
                            .section {
                                margin-bottom: 30px;
                                padding-bottom: 20px;
                                border-bottom: 2px solid #E8E8E8;
                            }
                            .section:last-child {
                                border-bottom: none;
                            }
                            .section h2 {
                                color: #512479;
                                margin-bottom: 15px;
                                font-size: 20px;
                            }
                            .interactive-chart {
                                background: linear-gradient(135deg, #F5F0FF 0%, #EBF4FF 100%);
                                border-radius: 12px;
                                padding: 20px;
                                margin: 15px 0;
                                text-align: center;
                                cursor: pointer;
                                transition: all 0.3s ease;
                            }
                            .interactive-chart:hover {
                                background: linear-gradient(135deg, #EBF4FF 0%, #F5F0FF 100%);
                                transform: scale(1.02);
                            }
                            .chart-bar {
                                display: flex;
                                align-items: flex-end;
                                justify-content: space-around;
                                height: 150px;
                                margin: 20px 0;
                            }
                            .bar {
                                width: 40px;
                                background: linear-gradient(180deg, #3C55E6 0%, #768BFF 100%);
                                border-radius: 8px 8px 0 0;
                                cursor: pointer;
                                transition: all 0.3s ease;
                            }
                            .bar:hover {
                                filter: brightness(1.2);
                                transform: translateY(-10px);
                            }
                            .interactive-table {
                                width: 100%;
                                border-collapse: collapse;
                                margin: 15px 0;
                            }
                            .interactive-table th {
                                background: linear-gradient(90deg, #3C55E6 0%, #768BFF 100%);
                                color: white;
                                padding: 12px;
                                text-align: left;
                            }
                            .interactive-table td {
                                padding: 12px;
                                border-bottom: 1px solid #E8E8E8;
                            }
                            .interactive-table tr:hover {
                                background: #F9F9F9;
                            }
                            button {
                                background: linear-gradient(90deg, #FF7401 0%, #E20262 100%);
                                color: white;
                                border: none;
                                padding: 10px 20px;
                                border-radius: 8px;
                                cursor: pointer;
                                margin: 10px 5px;
                                font-weight: 600;
                                transition: all 0.3s ease;
                            }
                            button:hover {
                                transform: translateY(-2px);
                                box-shadow: 0 5px 15px rgba(255, 116, 1, 0.3);
                            }
                        </style>
                    </head>
                    <body>
                        <div class="container">
                            <h1>📊 Interactive Analysis Dashboard</h1>

                            <div class="section">
                                <h2>Performance Metrics</h2>
                                <div class="interactive-chart">
                                    <p>Click on bars to see detailed information</p>
                                    <div class="chart-bar">
                                        <div class="bar" style="height: 60%; cursor: pointer;" onclick="alert('Accuracy: 87%')"></div>
                                        <div class="bar" style="height: 75%; cursor: pointer;" onclick="alert('Relevance: 92%')"></div>
                                        <div class="bar" style="height: 85%; cursor: pointer;" onclick="alert('Completeness: 95%')"></div>
                                        <div class="bar" style="height: 72%; cursor: pointer;" onclick="alert('Reliability: 78%')"></div>
                                    </div>
                                </div>
                            </div>

                            <div class="section">
                                <h2>Data Summary Table</h2>
                                <table class="interactive-table">
                                    <thead>
                                        <tr>
                                            <th>Metric</th>
                                            <th>Value</th>
                                            <th>Status</th>
                                            <th>Action</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>Data Points</td>
                                            <td>1,256</td>
                                            <td>✅ Complete</td>
                                            <td><button onclick="alert('Details for Data Points')">Details</button></td>
                                        </tr>
                                        <tr>
                                            <td>Insights Found</td>
                                            <td>42</td>
                                            <td>✅ Complete</td>
                                            <td><button onclick="alert('Details for Insights')">Details</button></td>
                                        </tr>
                                        <tr>
                                            <td>Analysis Time</td>
                                            <td>2.5 min</td>
                                            <td>✅ Complete</td>
                                            <td><button onclick="alert('Details for Time')">Details</button></td>
                                        </tr>
                                        <tr>
                                            <td>Quality Score</td>
                                            <td>4.8/5</td>
                                            <td>✅ Excellent</td>
                                            <td><button onclick="alert('Details for Quality')">Details</button></td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>

                            <div class="section">
                                <h2>Export & Share</h2>
                                <button onclick="window.print()">🖨️ Print Document</button>
                                <button onclick="alert('Sharing options would appear here')">📤 Share Results</button>
                                <button onclick="window.close()">❌ Close</button>
                            </div>
                        </div>
                    </body>
                    </html>
                `);
        interactiveWindow.document.close();

        btn.innerHTML = originalHTML;
        btn.disabled = false;
    }, 2000);
}