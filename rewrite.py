import re

html_path = "index.html"
css_path = "styles.css"

with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Navigation and Footer links
html = html.replace('href="#coleccion" class="nav-link">Colección</a>', 'href="#clientes" class="nav-link">Clientes</a>')
html = html.replace('href="#coleccion" class="btn btn-outline btn-large">Ver Catálogo</a>', 'href="#servicios" class="btn btn-outline btn-large">Ver Servicios</a>')
html = html.replace('href="#coleccion" class="btn btn-outline btn-small">Ver Colección</a>', 'href="#servicios" class="btn btn-outline btn-small">Ver Más</a>')
html = html.replace('href="#coleccion" class="btn btn-outline btn-small">Ver Catálogo</a>', 'href="#servicios" class="btn btn-outline btn-small">Ver Más</a>')

# Update "Ver Catálogo" in hero actions just in case
html = html.replace('<a href="#coleccion" class="btn btn-outline btn-large">Ver Catálogo</a>', '<a href="#servicios" class="btn btn-outline btn-large">Ver Servicios</a>')

# 2. Add 2 new services to the grid
service7_and_8 = """
                <!-- Service 7 -->
                <div class="flip-card stagger-item">
                    <div class="flip-card-inner">
                        <div class="flip-card-front glass-panel">
                            <img src="images/service_2_notext_1778808754689.png" alt="Arreglo de Joyas" class="card-img">
                            <div class="card-front-content">
                                <h3>Arreglo de Joyas</h3>
                                <span class="explore-text">Explorar <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
                            </div>
                        </div>
                        <div class="flip-card-back glass-panel">
                            <h3>Arreglo de Joyas</h3>
                            <p>Restauramos y reparamos tus joyas más preciadas, devolviéndoles su brillo y esplendor original con el mayor cuidado.</p>
                            <a href="#contacto" class="btn btn-outline btn-small">Cotizar Arreglo</a>
                        </div>
                    </div>
                </div>

                <!-- Service 8 -->
                <div class="flip-card stagger-item">
                    <div class="flip-card-inner">
                        <div class="flip-card-front glass-panel">
                            <img src="images/service_4_notext_1778808778996.png" alt="Arreglo de Relojes" class="card-img">
                            <div class="card-front-content">
                                <h3>Arreglo de Relojes</h3>
                                <span class="explore-text">Explorar <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg></span>
                            </div>
                        </div>
                        <div class="flip-card-back glass-panel">
                            <h3>Arreglo de Relojes</h3>
                            <p>Mantenimiento y reparación de relojes de alta gama. Nuestros especialistas aseguran precisión y funcionamiento óptimo.</p>
                            <a href="#contacto" class="btn btn-outline btn-small">Cotizar Arreglo</a>
                        </div>
                    </div>
                </div>
            </div>
"""
# Replace the end of the services grid with the new services and the closing div
html = html.replace('                </div>\n            </div>\n        </div>\n    </section>', service7_and_8 + '        </div>\n    </section>')

# 3. Update the 6 existing services to use the _notext versions
html = html.replace('service_1_1778801374185.png', 'service_1_notext_1778808741509.png')
html = html.replace('service_2_1778801388859.png', 'service_2_notext_1778808754689.png')
html = html.replace('service_3_1778801403738.png', 'service_3_notext_1778808767619.png')
html = html.replace('service_4_1778801418284.png', 'service_4_notext_1778808778996.png')
html = html.replace('service_5_1778801435332.png', 'service_5_notext_1778808794807.png')
html = html.replace('service_6_1778801449929.png', 'service_6_notext_1778808808755.png')


# 4. Insert Clientes Section before CTA Section
clientes_section = """
    <!-- Clientes Section -->
    <section class="testimonials section" id="clientes">
        <div class="container">
            <div class="section-header text-center fade-up">
                <span class="badge">Nuestros Clientes</span>
                <h2 class="section-title">Reseñas de <span class="gold-text">Google Maps</span></h2>
            </div>
            <div class="grid testimonials-grid fade-up" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
                <!-- Review 1 -->
                <div class="review-card glass-panel" style="padding: 2rem;">
                    <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                        <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--gold-primary); display: flex; align-items: center; justify-content: center; font-weight: bold; color: #000; font-size: 1.25rem; margin-right: 1rem;">E</div>
                        <div>
                            <h4 style="margin: 0; line-height: 1.2;">Elias Ortega</h4>
                            <span style="font-size: 0.8rem; color: var(--text-secondary);">Hace 5 meses</span>
                        </div>
                    </div>
                    <div style="color: var(--gold-primary); margin-bottom: 1rem;">
                        ★ ★ ★ ★ ★
                    </div>
                    <p style="color: var(--text-secondary); font-style: italic;">"Excelente servicio unos capos me soldaron joyas de un día para otro recomendado"</p>
                </div>
                <!-- Review 2 -->
                <div class="review-card glass-panel" style="padding: 2rem;">
                    <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                        <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--gold-primary); display: flex; align-items: center; justify-content: center; font-weight: bold; color: #000; font-size: 1.25rem; margin-right: 1rem;">A</div>
                        <div>
                            <h4 style="margin: 0; line-height: 1.2;">AndresIG IG</h4>
                            <span style="font-size: 0.8rem; color: var(--text-secondary);">Hace 2 años</span>
                        </div>
                    </div>
                    <div style="color: var(--gold-primary); margin-bottom: 1rem;">
                        ★ ★ ★ ★ ★
                    </div>
                    <p style="color: var(--text-secondary); font-style: italic;">"Excelente atención!!! y excelente calidad recomendable muy buenos precios y excelentes profesionales."</p>
                </div>
                <!-- Review 3 -->
                <div class="review-card glass-panel" style="padding: 2rem;">
                    <div style="display: flex; align-items: center; margin-bottom: 1rem;">
                        <div style="width: 48px; height: 48px; border-radius: 50%; background: var(--gold-primary); display: flex; align-items: center; justify-content: center; font-weight: bold; color: #000; font-size: 1.25rem; margin-right: 1rem;">G</div>
                        <div>
                            <h4 style="margin: 0; line-height: 1.2;">Gabriela Becerra</h4>
                            <span style="font-size: 0.8rem; color: var(--text-secondary);">Hace 7 años</span>
                        </div>
                    </div>
                    <div style="color: var(--gold-primary); margin-bottom: 1rem;">
                        ★ ★ ★ ★ ★
                    </div>
                    <p style="color: var(--text-secondary); font-style: italic;">"Joyeria de super confianza y atención, años comprando y haciendo arreglos alli en su taller. Siempre agradecida por su delicadeza. Totalmente recomendado."</p>
                </div>
            </div>
        </div>
    </section>

    <!-- CTA Section -->"""

html = html.replace('    <!-- CTA Section -->', clientes_section)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

# Now for styles.css, ensure the services grid adapts strictly
css_update = """

/* =========================================
   UPDATES PARA SERVICIOS Y CLIENTES
   ========================================= */
.services-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 2rem;
}

@media (max-width: 1200px) {
    .services-grid { grid-template-columns: repeat(3, 1fr); }
}

@media (max-width: 900px) {
    .services-grid { grid-template-columns: repeat(2, 1fr); }
}

@media (max-width: 600px) {
    .services-grid { grid-template-columns: 1fr; }
}
"""

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Only append if not already there
if "UPDATES PARA SERVICIOS Y CLIENTES" not in css:
    with open(css_path, "a", encoding="utf-8") as f:
        f.write(css_update)

print("Files updated successfully")
