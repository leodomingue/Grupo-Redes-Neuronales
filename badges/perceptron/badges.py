from IPython.display import display, HTML


def lanzar_confeti_cartografo():
    js_confetti = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        confetti({
            particleCount: 150,
            spread: 70,
            origin: { y: 0.6 },
            colors: ['#856404', '#d4af37', '#fdf6e3', '#8d6e63']
        });
    </script>
    """
    display(HTML(js_confetti))

def badge_cartografo():
    html_code = """
    <div style="
        background-color: #fdf6e3;
        border: 4px double #856404;
        padding: 25px;
        border-radius: 10px;
        color: #5d4037;
        font-family: 'Garamond', serif;
        text-align: center;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
        max-width: 500px;
        margin: 20px auto;
        position: relative;
    ">
        <div style="font-size: 50px; margin-bottom: 10px;">📍🗺️📜</div>
        <h2 style="margin: 0; font-size: 24px; color: #8d6e63; text-transform: uppercase; letter-spacing: 2px;">
            CARTÓGRAFO DE DATOS
        </h2>
        <p style="font-size: 15px; font-style: italic; margin-top: 10px; color: #6d4c41; line-height: 1.5;">
            "He visto los puntos dispersos  y he trazado el límite." <br>
        </p>
        <hr style="border: 0; border-top: 1px solid rgba(0,0,0,0.2); margin: 15px 0;">
        <div style="font-size: 12px; font-weight: bold; color: #8d6e63;">
            Aprendiste a trazar rectas como hiperplano
        </div>

    </div>
    """
    display(HTML(html_code))
    lanzar_confeti_cartografo()


def lanzar_confeti_volcanico():
    js_confetti = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        confetti({
            particleCount: 150,
            spread: 80,
            origin: { y: 0.6 },
            colors: ['#856404', '#e67e22', '#fdf6e3', '#d35400'] // Oro viejo, Naranja lava, Crema, Terracota
        });
    </script>
    """
    display(HTML(js_confetti))


def badge_remapeo_dimensional():
    html_code = """
    <div style="
        background-color: #fdf6e3; 
        border: 4px double #856404; 
        padding: 25px;
        border-radius: 10px;
        color: #5d4037; 
        font-family: 'Garamond', serif; 
        text-align: center;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.2); 
        max-width: 500px;
        margin: 20px auto;
        position: relative;
    ">
        <div style="font-size: 50px; margin-bottom: 10px;">🌋🗺️</div> 
        <h2 style="margin: 0; font-size: 24px; color: #8d6e63; text-transform: uppercase; letter-spacing: 2px;">
            ESPECIALISTA EN REMAPEO DIMENSIONAL
        </h2>
        <p style="font-size: 15px; font-style: italic; margin-top: 10px; color: #6d4c41;">
            "El volcán ya no es un problema de curvas, es un problema de una línea bien trazada. <br>
            ¡El espacio ha sido redefinido!"
        </p>
        <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.3); margin: 15px 0;">
        <div style="font-size: 13px; font-weight: bold; text-transform: uppercase;">
            Has aprendido a redimensionar el espacio original a uno con otra norma
        </div>
    </div>
    """
    display(HTML(html_code))
    lanzar_confeti_volcanico()


def lanzar_confeti_aeroterra():
    js_confetti = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        confetti({
            particleCount: 150,
            spread: 80,
            origin: { y: 0.6 },
            colors: ['#856404', '#e67e22', '#fdf6e3', '#d35400'] 
        });
    </script>
    """
    display(HTML(js_confetti))

def badge_aeroterra():
    html_code = """
    <div style="
        background: linear-gradient(135deg, #1e5d28 0%, #2ecc71 100%);
        padding: 25px;
        border-radius: 20px;
        color: white;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        border: 2px solid #f1c40f;
        max-width: 500px;
        margin: 20px auto;
    ">
        <div style="font-size: 50px; margin-bottom: 10px;">🌱🛸</div>
        <h2 style="margin: 0; font-size: 22px; color: #f1c40f;">
            AEROTERRA
        </h2>
        <h2 style="margin: 0; font-size: 18px; color: #f1c40f; text-transform: uppercase;">
            ¡MISIÓN: DE DESIERTO A JUNGLA EN O(n)!
        </h2>
        <p style="font-size: 16px; font-style: italic; margin-top: 10px;">
            "El Perceptrón ha hablado: Ya sabemos dónde regar y dónde tirar químicos."
        </p>
        <hr style="border: 0; border-top: 1px solid rgba(255,255,255,0.3); margin: 15px 0;">
        <div style="font-size: 13px; font-weight: bold; text-transform: uppercase;">
            Has aprendido a realizar hiperplanos con features de imagenes
        </div>
    </div>
    """
    display(HTML(html_code))
    lanzar_confeti_aeroterra()


def lanzar_confeti_bits():
    js_confetti = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        confetti({
            particleCount: 120,
            spread: 90,
            origin: { y: 0.6 },
            colors: ['#00ff41', '#333333', '#ffffff'] 
        });
    </script>
    """
    display(HTML(js_confetti))

def badge_maestro_del_filtro():
    html_code = """
    <div style="
        background-color: #1a1a1a; 
        border: 4px solid #00ff41; 
        padding: 30px;
        border-radius: 12px;
        color: #e0e0e0;
        font-family: 'Consolas', 'Courier New', monospace; 
        text-align: center;
        box-shadow: 0 0 25px rgba(0,255,65,0.4); 
        max-width: 550px;
        margin: 20px auto;
        position: relative;
    ">
        <div style="font-size: 50px; margin-bottom: 10px; color: #00ff41;">⌨️💾🐧</div> 
        <h2 style="margin: 0; font-size: 26px; color: #00ff41; text-transform: uppercase; letter-spacing: 2px;">
            MAESTRO DEL FILTRO BINARIO
        </h2>
        <p style="font-size: 16px; font-style: italic; margin-top: 15px; color: #cccccc;">
            "El Oráculo Algorítmico ha hablado. <br>
            Los dignos han sido separados de los falsos. <br>
            ¡Acceso concedido a The Gigabyte Guild!"
        </p>
        <hr style="border: 0; border-top: 1px solid rgba(46, 204, 113, 0.3); margin: 15px 0;">
        <div style="font-size: 12px; font-weight: bold; color: #27ae60;">
            Has aprendido a crear hiperplanos en más dimensiones
        </div>

    </div>
    """
    display(HTML(html_code))
    lanzar_confeti_bits()


def badge_cero_infinito_auris():
    js = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        confetti({
            particleCount: 150,
            spread: 80,
            origin: { y: 0.7 },
            colors: ['#2ecc71', '#ffffff', '#95a5a6']
        });
    </script>
    """
    
    html = """
    <div style="
        background: linear-gradient(135deg, #ffffff 0%, #e0e0e0 100%);
        border: 2px solid #2ecc71;
        padding: 25px;
        border-radius: 20px;
        color: #2c3e50;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
        text-align: center;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        max-width: 550px;
        margin: 20px auto;
        border-bottom: 6px solid #27ae60;
    ">
        <div style="font-size: 50px; margin-bottom: 10px;">🎧🏛️</div>
        <h2 style="margin: 0; font-size: 22px; color: #27ae60; text-transform: uppercase; letter-spacing: 1px;">
            LOGRO: EQUILIBRIO EN EL CERO + INFINITO
        </h2>
        <p style="font-size: 15px; font-style: italic; margin-top: 10px; color: #7f8c8d;">
            "Has logrado lo imposible: <br>
            que ese cable roto funcione mediante lógica de capas."
        </p>
        <hr style="border: 0; border-top: 1px solid rgba(46, 204, 113, 0.3); margin: 15px 0;">
        <div style="font-size: 12px; font-weight: bold; color: #27ae60;">
            Has aprendido a crear sistemas especializados con más de una capa
        </div>
    </div>
    """
    display(HTML(js + html))

