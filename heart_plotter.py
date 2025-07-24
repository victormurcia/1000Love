import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import random
import time
import json

# Set wide layout
st.set_page_config(layout="wide")
st.title("💖 1000 Love")

if "app_started" not in st.session_state:
    st.session_state.app_started = False

if not st.session_state.app_started:
    # Only show typewriter if we haven't shown it yet
    if "typewriter_shown" not in st.session_state:
        st.session_state.typewriter_shown = False
    
    if not st.session_state.typewriter_shown:
        # 1) Run the typewriter greeting
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        typewriter_text = """Wassup my Mooncakes <3
Press the button below to watch 1000 hearts drawn for you while one of the many songs we've shared over the last 5 years plays for you.
I love you alotl axolotl!


⠀⠀⠀⠀⠀⠀⣀⣀⠀⣀⣠⡴⠲⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣼⠁⠈⠻⣯⠏⠀⠀⠘⡗⢶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣀⣽⡀⠀⠀⢸⡄⠀⠀⣠⡷⠚⠉⠉⣟⡷⢦⡄⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠸⣅⣈⣿⣄⡐⣾⣷⣧⣼⣋⠄⠀⢀⡴⢯⠙⢶⣽⡆⠀⠀⣀⣀⣴⠋⠀⢹⣤⣤⡀⠀⠀⠀⠀
⠀⠀⢠⠞⠉⠀⢤⣭⣿⣿⣿⣿⣿⣷⣖⠛⠛⢦⡾⠶⠼⣌⡿⠒⠶⢿⣟⣇⢰⣴⡏⡀⢨⡗⠋⠉⢹⡄
⠀⠀⢧⣀⣀⣠⣤⣼⣿⣿⣿⣿⣿⣧⡀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀⠀⠈⠻⢿⣿⡛⢷⣾⣴⣂⣤⣞⠀
⠀⢠⣾⣿⣴⠏⠐⢋⡿⣿⣿⢿⠀⢹⡍⢻⠲⠶⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⠼⣿⡥⠄⠀⢈⡷
⢠⣿⣿⠉⣿⠀⢀⡾⠑⠋⢇⠈⠀⢸⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⣼⢷⣶⡖⠻⣄
⠘⣿⠘⣄⣸⡷⣿⣧⠀⠀⢸⣆⣀⡼⠙⠿⠶⠶⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣾⡖⢉⣼⢧⣀⠀⢹
⠀⠙⢦⡞⠉⠀⣷⡾⢦⣠⣾⡿⣿⠁⠀⠈⠀⠀⠀⠐⠦⠤⠤⢤⡀⠀⠀⢠⣿⣧⠈⣿⣟⠛⠈⡏⠉⠉
⠀⠀⠀⠀⠀⠀⠙⠧⣾⣀⡽⠾⣏⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠀⠈⠿⠟⢠⡏⣹⠓⠚⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⢨⡏⠈⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠈⠙⠒⠂⠀⠀⢤⣀⣀⣀⣤⠤⣶⣿⠟⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⡞⠁⠀⠀⣴⠀⠀⢻⣆⠀⠀⠈⢳⣴⡿⠋⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠀⠀⠀⡼⠁⠀⢀⠀⠙⢿⠢⡄⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⠈⠀⠀⠀⠷⣤⡏⠙⠆⠀⢸⡇⠸⣆⠀⢀⣠⠤⠤⣄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡛⠁⠀⣀⣀⣀⣠⡿⠦⠤⠴⣾⡁⠀⠈⠉⠁⠀⢀⡀⠀⠉⠢⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠚⣿⡟⠁⢹⠀⠀⠀⠀⠀⠉⠓⠲⠒⠚⠉⠉⠉⠙⢦⡀⢱
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⡄⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠒⠒⠢⣧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢷⡀⠙⠦⣈⡳⣤⣀⣀⣀⣀⡴⢞⡯⠖⠚⠙⠲⣄⠀⢸
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠉⠁⠉⠉⣉⡥⠞⠉⠀⠀⠀⠀⠀⠸⡆⡾
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠒⠒⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠁

"""
        container = st.empty()
        msg = ""
        for ch in typewriter_text:
            msg += ch
            container.markdown(
                f"<div style='font-family: monospace; font-size:16px; white-space: pre-wrap;'>{msg}</div>",
                unsafe_allow_html=True
            )
            time.sleep(0.01)
        st.markdown("</div>", unsafe_allow_html=True)
        st.session_state.typewriter_shown = True
    else:
        # Show the final message without typewriter effect
        st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
        st.markdown(
            f"<div style='font-family: monospace; font-size:16px; white-space: pre-wrap;'>Wassup my Mooncakes <3\nPress the button below to watch 1000 hearts drawn for you while one of the many songs we've shared over the last 5 years plays for you.\nI love you alotl axolotl!</div>",
            unsafe_allow_html=True
        )
        st.markdown("</div>", unsafe_allow_html=True)
    
    # 2) Show the button *after* the typewriter
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💘 Start Your 1000 Loves", key="start_button"):
            st.session_state.app_started = True
            st.rerun()
    
    # 3) Stop so nothing else renders until they click
    st.stop()

if st.session_state.app_started:
    # === Sidebar ===
    with st.sidebar:
        st.header("📝 About This App")
        st.write(
            """
            Wassup my Mooncakes <3

            The other day you told me that I owe you 1000 loves. You never clarified what that means, so here's my attempt at delivering.

            Press the button below to watch 1000 hearts drawn for you while one of the many songs we've shared with each other over the last 5 years plays for you.

            Since I know you'll appreciate here's how it works:

            I'm using the parametric equation for a heart but varying the coeffiecients (I experimented with them to make sure that they'd most combinations would at produce something akin to a cardioid shape).

            I precompute 1000 traces at a time and then 'sketch' 10 of them in real time in each plot. Since there's a 10 x 10 grid, we have 1000 unique hearts made for you every time :)

            The music comes from a playlist I made with 100+ songs we've shared with each other over the years.

            I love you alotl axolotl!
           
            """
        )
        st.latex(r"""
            \begin{align*}
            x(t) &= 16 \sin^3(t) \\
            y(t) &= a_1 \cos(t) + a_2 \cos(2t) + a_3 \cos(3t) + a_4 \cos(4t)
            \end{align*}
        """)
        # Centered GIF using markdown+HTML
        st.markdown(
            """
            <div style="display: flex; justify-content: center;">
                <img src="https://media1.tenor.com/m/OQgefkPJ_dYAAAAd/fill-my.gif" width="250">
            </div>
            """,
            unsafe_allow_html=True
        )
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            generate = st.button("🎲 Generate")
        
        if generate:
            # === Load playlist from JSON and show a random video ===
            try:
                with open("playlist_videos.json", "r", encoding="utf-8") as f:
                    playlist = json.load(f)
                title, video_id = random.choice(list(playlist.items()))
                st.markdown("---")
                st.subheader("🎬 Now playing:")
                st.video(f"https://www.youtube.com/watch?v={video_id}", autoplay=True)
            except Exception as e:
                st.warning("Couldn't load the playlist video.")
                st.error(str(e))

    # === Constants ===
    n_rows, n_cols = 10, 10
    n_traces = 10
    num_points = 200
    step = 2
    delay = 0.003
    palette = [
        "#8B0000", "#7D0C0C", "#4A010F", "#FF1493", "#9400D3",
        "#8A2BE2", "#6A5ACD", "#9229DC", "#006400", "#2E8B57",
        "#20B2AA", "#4B0082", "#D02090", "#CD5C5C", "#0D1F0D",
        "#2E4907", "#3D0B88", "#BA55D3", "#9370DB", "#380810"
    ]
    a1_range = (5.0, 20.0)
    a2_range = (-20.0, 20.0)
    a3_range = (-20.0, 20.0)
    a4_range = (-20.0, 20.0)
    t = np.linspace(0, 2 * np.pi, num_points)
    x_base = 16 * np.sin(t) ** 3

    if generate:
        # === Precompute Traces ===
        traces_grid = []
        all_y = []
        for _ in range(n_rows * n_cols):  # Fixed: was "* in range(n*rows * n_cols)"
            trace_list = []
            for _ in range(n_traces):  # Fixed: was "* in range(n*traces)"
                a1 = np.random.uniform(*a1_range)
                a2 = np.random.uniform(*a2_range)
                a3 = np.random.uniform(*a3_range)
                a4 = np.random.uniform(*a4_range)
                y = a1 * np.cos(t) + a2 * np.cos(2 * t) + a3 * np.cos(3 * t) + a4 * np.cos(4 * t)
                color = random.choice(palette)
                trace_list.append((y, color))
                all_y.append(y)
            traces_grid.append(trace_list)
        
        xlim = (x_base.min() - 2, x_base.max() + 2)
        ylim = (np.min(all_y) - 2, np.max(all_y) + 2)
        
        # === Setup Figure ===
        placeholder = st.empty()
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(8, 15), dpi=100, facecolor="black")
        axes = axes.flatten()
        
        # Draw once, reuse Line2D objects
        lines_grid = []
        for ax_idx, ax in enumerate(axes):
            ax.set_facecolor("black")
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)
            ax.axis("off")
            ax.set_aspect("equal")
            line_objs = []
            for y, color in traces_grid[ax_idx]:
                line, = ax.plot([], [], color=color, linewidth=1.0, alpha=0.8)
                line_objs.append(line)
            lines_grid.append(line_objs)
        
        fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)
        
        # === Animate ===
        for i in range(step, num_points + 1, step):
            for ax_idx, line_objs in enumerate(lines_grid):
                for j, line in enumerate(line_objs):
                    y = traces_grid[ax_idx][j][0]
                    line.set_data(x_base[:i], y[:i])
            placeholder.pyplot(fig, use_container_width=False)
            time.sleep(delay)
        
        #st.success("All hearts drawn across the grid 💘")
    else:
        st.write("Use the sidebar to generate a magical heart grid ✨")