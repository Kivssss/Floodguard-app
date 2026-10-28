import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_architecture():
    # Set high DPI and figure size for publication-grade clarity
    fig, ax = plt.subplots(figsize=(14, 9), dpi=300)
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    # Color Palette (Modern Tech / Professional Academic)
    primary_blue = '#1E40AF'      # Tailwind blue-800
    card_blue = '#EFF6FF'         # Light blue
    border_blue = '#3B82F6'

    primary_emerald = '#065F46'   # Emerald
    card_emerald = '#ECFDF5'
    border_emerald = '#10B981'

    primary_amber = '#92400E'     # Amber
    card_amber = '#FFFBEB'
    border_amber = '#F59E0B'

    primary_purple = '#5B21B6'    # Purple
    card_purple = '#F5F3FF'
    border_purple = '#8B5CF6'

    # Title Banner
    ax.text(7.0, 8.6, "PROJECT NEXUS: FLOODGUARD SYSTEM ARCHITECTURE", 
            ha='center', va='center', fontsize=18, fontweight='bold', color='#0F172A', fontfamily='sans-serif')
    ax.text(7.0, 8.25, "End-to-End System Integration: Native Mobile, FastAPI Backend, SQLite & Cloud Services", 
            ha='center', va='center', fontsize=11, color='#475569', fontfamily='sans-serif')

    # 1. FRONTEND BOX (Left Side)
    # [x, y, w, h]
    frontend_box = patches.FancyBboxPatch((0.6, 1.8), 3.8, 5.9,
                                          boxstyle="round,pad=0.2,rounding_size=0.15",
                                          ec=border_blue, fc=card_blue, lw=2)
    ax.add_patch(frontend_box)
    ax.text(2.5, 7.45, "MOBILE FRONTEND (CLIENT)", ha='center', va='center', 
            fontsize=12, fontweight='bold', color=primary_blue)
    ax.text(2.5, 7.15, "Native Android (Kotlin 2.2 / Jetpack Compose)", ha='center', va='center', 
            fontsize=8.5, color='#1E3A8A', fontstyle='italic')

    # Frontend Inner Modules
    fe_items = [
        ("UI & Presentation Layer", "Jetpack Compose, Material 3, ViewBinding\nDashboard, Report, Alerts, Map Activities", 6.2),
        ("Embedded GIS Map Engine", "Leaflet.js in Android WebView\nSan Mateo Hazard GeoJSON Layer", 4.9),
        ("Local Persistence Mirror", "SQLiteOpenHelper (FloodGuardDatabase v8)\nOffline Credentials & Cached Reports", 3.6),
        ("REST Communication Client", "FloodGuardApiService (Background Threads)\nJSON Serialization & Dynamic Host Routing", 2.3)
    ]
    for title, desc, y_pos in fe_items:
        rect = patches.FancyBboxPatch((0.85, y_pos - 0.45), 3.3, 0.9,
                                      boxstyle="round,pad=0.1,rounding_size=0.08",
                                      ec='#93C5FD', fc='#FFFFFF', lw=1.2)
        ax.add_patch(rect)
        ax.text(2.5, y_pos + 0.15, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#1E3A8A')
        ax.text(2.5, y_pos - 0.18, desc, ha='center', va='center', fontsize=7.5, color='#334155')

    # 2. BACKEND BOX (Center)
    backend_box = patches.FancyBboxPatch((5.1, 3.2), 4.0, 4.5,
                                         boxstyle="round,pad=0.2,rounding_size=0.15",
                                         ec=border_emerald, fc=card_emerald, lw=2)
    ax.add_patch(backend_box)
    ax.text(7.1, 7.45, "REST API BACKEND SERVER", ha='center', va='center', 
            fontsize=12, fontweight='bold', color=primary_emerald)
    ax.text(7.1, 7.15, "FastAPI v0.143 / Uvicorn ASGI / Python 3.14", ha='center', va='center', 
            fontsize=8.5, color='#064E3B', fontstyle='italic')

    be_items = [
        ("REST API Routes & Security", "Endpoints: /api/auth, /api/reports, /api/mapping\nCase-insensitive Auth, PH Mobile Normalizer", 6.2),
        ("Pydantic Data Schemas", "Strict Inbound / Outbound Type Enforcement\nPayload Verification & Base64 Handling", 4.9),
        ("SQLAlchemy ORM Engine", "Session Management, Table Mappings\nAutomated Schema Startup Migrations", 3.6)
    ]
    for title, desc, y_pos in be_items:
        rect = patches.FancyBboxPatch((5.35, y_pos - 0.45), 3.5, 0.9,
                                      boxstyle="round,pad=0.1,rounding_size=0.08",
                                      ec='#A7F3D0', fc='#FFFFFF', lw=1.2)
        ax.add_patch(rect)
        ax.text(7.1, y_pos + 0.15, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#064E3B')
        ax.text(7.1, y_pos - 0.18, desc, ha='center', va='center', fontsize=7.5, color='#334155')

    # 3. DATABASE BOX (Center Bottom)
    db_box = patches.FancyBboxPatch((5.1, 0.7), 4.0, 1.9,
                                    boxstyle="round,pad=0.2,rounding_size=0.15",
                                    ec=border_amber, fc=card_amber, lw=2)
    ax.add_patch(db_box)
    ax.text(7.1, 2.3, "CENTRAL RELATIONAL DATABASE", ha='center', va='center', 
            fontsize=11.5, fontweight='bold', color=primary_amber)
    ax.text(7.1, 2.05, "Embedded SQLite (floodguard.db)", ha='center', va='center', 
            fontsize=8.5, color='#78350F', fontstyle='italic')

    db_sub = patches.FancyBboxPatch((5.35, 0.85), 3.5, 0.95,
                                    boxstyle="round,pad=0.1,rounding_size=0.08",
                                    ec='#FDE68A', fc='#FFFFFF', lw=1.2)
    ax.add_patch(db_sub)
    ax.text(7.1, 1.45, "Tables: users | reports | roads | alerts", ha='center', va='center', fontsize=9, fontweight='bold', color='#78350F')
    ax.text(7.1, 1.12, "Relational Constraints, Phone Uniqueness Indexes\nACID Transactional Data Integrity", ha='center', va='center', fontsize=7.5, color='#334155')

    # 4. EXTERNAL & CLOUD APIS (Right Side)
    cloud_box = patches.FancyBboxPatch((9.8, 1.8), 3.6, 5.9,
                                       boxstyle="round,pad=0.2,rounding_size=0.15",
                                       ec=border_purple, fc=card_purple, lw=2)
    ax.add_patch(cloud_box)
    ax.text(11.6, 7.45, "EXTERNAL CLOUD SERVICES", ha='center', va='center', 
            fontsize=12, fontweight='bold', color=primary_purple)
    ax.text(11.6, 7.15, "AI Vision, Telemetry & Push Notification APIs", ha='center', va='center', 
            fontsize=8.5, color='#4C1D95', fontstyle='italic')

    ext_items = [
        ("Google Gemini Multimodal AI", "Models: 3.5-flash / 3.8-flash\nAuto Photo Verification & Depth Estimation\nRejects Memes / Fake Flood Images", 5.9),
        ("Open-Meteo Forecast API", "v1 Meteorological Telemetry\nReal-time Precipitation, Hourly Rain Probability\nSan Mateo Weather Metrics", 4.1),
        ("Firebase Cloud Messaging", "Firebase Admin SDK / Topic 'floodguard'\nInstant High-Severity Inundation Alerts\nPush Broadcast to All Active Users", 2.3)
    ]
    for title, desc, y_pos in ext_items:
        rect = patches.FancyBboxPatch((10.05, y_pos - 0.65), 3.1, 1.3,
                                      boxstyle="round,pad=0.1,rounding_size=0.08",
                                      ec='#DDD6FE', fc='#FFFFFF', lw=1.2)
        ax.add_patch(rect)
        ax.text(11.6, y_pos + 0.35, title, ha='center', va='center', fontsize=9.5, fontweight='bold', color='#4C1D95')
        ax.text(11.6, y_pos - 0.15, desc, ha='center', va='center', fontsize=7.5, color='#334155')

    # --- CONNECTING ARROWS & ANNOTATIONS ---
    # Frontend <-> Backend
    ax.annotate("", xy=(5.05, 5.2), xytext=(4.45, 5.2),
                arrowprops=dict(arrowstyle="<->", color='#0284C7', lw=2.5))
    ax.text(4.75, 5.5, "HTTP/REST\n(JSON)", ha='center', va='center', fontsize=8, fontweight='bold', color='#0369A1')

    # Backend <-> Database
    ax.annotate("", xy=(7.1, 3.15), xytext=(7.1, 2.65),
                arrowprops=dict(arrowstyle="<->", color='#D97706', lw=2.5))
    ax.text(7.85, 2.9, "SQLAlchemy / SQL Queries", ha='center', va='center', fontsize=7.8, fontweight='bold', color='#B45309')

    # Backend -> Gemini AI
    ax.annotate("", xy=(9.75, 5.9), xytext=(9.15, 5.9),
                arrowprops=dict(arrowstyle="<->", color='#7C3AED', lw=2))
    ax.text(9.45, 6.2, "Base64\nPhoto", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#6D28D9')

    # Backend -> Open-Meteo
    ax.annotate("", xy=(9.75, 4.1), xytext=(9.15, 4.1),
                arrowprops=dict(arrowstyle="<->", color='#7C3AED', lw=2))
    ax.text(9.45, 4.4, "Weather\nSync", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#6D28D9')

    # Backend -> FCM
    ax.annotate("", xy=(9.75, 2.3), xytext=(9.15, 3.4),
                arrowprops=dict(arrowstyle="->", color='#7C3AED', lw=2))
    ax.text(9.45, 2.8, "Publish Alert", ha='center', va='center', fontsize=7.5, fontweight='bold', color='#6D28D9')

    # Direct push arrow FCM -> Frontend (Floating Notification)
    ax.annotate("", xy=(4.45, 2.0), xytext=(9.75, 2.0),
                arrowprops=dict(arrowstyle="->", color='#EF4444', lw=2, linestyle='dashed'))
    ax.text(7.1, 0.35, "Broadcast FCM Push Notification to App Topic ('floodguard')", 
            ha='center', va='center', fontsize=8.5, fontweight='bold', color='#DC2626')

    # Axis limits & cleanup
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 9)
    ax.axis('off')

    plt.tight_layout()
    output_png = "FloodGuard_System_Architecture.png"
    output_jpg = "FloodGuard_System_Architecture.jpg"
    plt.savefig(output_png, dpi=300, bbox_inches='tight')
    plt.savefig(output_jpg, dpi=300, bbox_inches='tight')
    print(f"Generated successfully: {output_png} and {output_jpg}")

if __name__ == "__main__":
    draw_architecture()
