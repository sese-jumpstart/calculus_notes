import numpy as np
import matplotlib.pyplot as plt

def generate_diagrams():
    # 1. Velocity Diagram
    fig, ax = plt.subplots(figsize=(5, 3.5))
    t = np.linspace(0, 2, 100)
    v = 1.5 * t
    ax.plot(t, v, color='#4A3B8A', lw=2.5)
    ax.set_xlabel('t', loc='right')
    ax.set_ylabel('v(t)', loc='top', rotation=0, labelpad=-10)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-0.2, 2.2)
    ax.set_ylim(-0.2, 3.5)
    ax.plot(2.2, 0, ">k", clip_on=False)
    ax.plot(0, 3.5, "^k", clip_on=False)
    plt.tight_layout()
    plt.savefig('fig1_velocity.png', dpi=300)
    plt.close()

    # 2. Position Diagram
    fig, ax = plt.subplots(figsize=(5, 3.5))
    t = np.linspace(0, 2, 100)
    y = 0.75 * t**2
    ax.plot(t, y, color='#4A3B8A', lw=2.5)
    
    t1, y1, m1 = 0.5, 0.75 * 0.5**2, 1.5 * 0.5
    t_seg1 = np.linspace(0.2, 0.9, 10)
    ax.plot(t_seg1, m1 * (t_seg1 - t1) + y1, color='#2E7D32', lw=2)
    ax.text(0.95, y1, 'small slope', color='#2E7D32', va='center')
    
    t2, y2, m2 = 1.7, 0.75 * 1.7**2, 1.5 * 1.7
    t_seg2 = np.linspace(1.4, 1.9, 10)
    ax.plot(t_seg2, m2 * (t_seg2 - t2) + y2, color='#2E7D32', lw=2)
    ax.text(1.3, y2 + 0.3, 'high\nslope', color='#2E7D32', ha='right')

    ax.set_xlabel('t', loc='right')
    ax.set_ylabel('y(t)', loc='top', rotation=0, labelpad=-10)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-0.2, 2.2)
    ax.set_ylim(-0.2, 3.5)
    ax.plot(2.2, 0, ">k", clip_on=False)
    ax.plot(0, 3.5, "^k", clip_on=False)
    plt.tight_layout()
    plt.savefig('fig2_position.png', dpi=300)
    plt.close()

    # 3. Derivative Concept Diagram
    fig, ax = plt.subplots(figsize=(5, 4.5))
    t = np.linspace(0.2, 2, 100)
    y = 0.5 * t**2 + 0.2 * t
    ax.plot(t, y, color='#4A3B8A', lw=2.5)
    t_pt, dt = 0.8, 0.8
    y_pt = 0.5 * t_pt**2 + 0.2 * t_pt
    y_dt = 0.5 * (t_pt + dt)**2 + 0.2 * (t_pt + dt)
    ax.plot([t_pt, t_pt+dt], [y_pt, y_dt], color='#2E7D32', lw=1.5, marker='x', markersize=8)
    ax.plot([t_pt, t_pt+dt], [y_pt, y_pt], 'k--', lw=1.5)
    ax.plot([t_pt+dt, t_pt+dt], [y_pt, y_dt], 'k--', lw=1.5)
    ax.text(t_pt + dt/2, y_pt - 0.2, r'$\Delta t$', ha='center', fontsize=12)
    ax.text(t_pt + dt + 0.05, (y_pt + y_dt)/2, r'$\Delta y$', va='center', fontsize=12)
    ax.text(t_pt, y_pt - 0.4, 't', ha='center')
    ax.set_xlabel('t', loc='right')
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(-0.1, 2.0)
    ax.set_ylim(-0.2, 2.5)
    ax.plot(2.0, 0, ">k", clip_on=False)
    ax.plot(0, 2.5, "^k", clip_on=False)
    plt.tight_layout()
    plt.savefig('fig3_derivative.png', dpi=300)
    plt.close()

    # 4. Unit Circle / Vector Diagram
    fig, ax = plt.subplots(figsize=(5, 5))
    theta_arc = np.linspace(0, np.pi/2 + 0.2, 100)
    ax.plot(np.cos(theta_arc), np.sin(theta_arc), 'k--', lw=1)
    theta = np.pi / 6
    x, y = np.cos(theta), np.sin(theta)
    ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color='#4A3B8A', width=0.015)
    dx, dy = -np.sin(theta), np.cos(theta)
    ax.quiver(x, y, dx, dy, angles='xy', scale_units='xy', scale=1, color='#D32F2F', width=0.015)
    ax.text(x*0.5, y*0.5 + 0.08, r'$\vec{y}$', color='#4A3B8A', fontsize=14)
    ax.text(x + dx*0.25 + 0.05, y + dy*0.25 + 0.05, r'$\frac{d\vec{y}}{dt}$', color='#D32F2F', fontsize=14)
    ax.text(0.2, 0.06, r'$\theta$', fontsize=12)
    box_len = 0.08
    bx1, by1 = x + dx*box_len, y + dy*box_len
    bx2, by2 = bx1 - x*box_len, by1 - y*box_len
    bx3, by3 = x - x*box_len, y - y*box_len
    ax.plot([bx1, bx2, bx3], [by1, by2, by3], color='black', lw=1)
    ax.text(bx2 - 0.05, by2 + 0.05, r'$90^\circ$', fontsize=10)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.set_xlim(-0.2, 1.5)
    ax.set_ylim(-0.2, 1.5)
    ax.set_aspect('equal')
    ax.set_xticks([1])
    ax.set_xticklabels(['1'])
    ax.set_yticks([])
    plt.tight_layout()
    plt.savefig('fig4_circle.png', dpi=300)
    plt.close()

    # 5. Exponential Plot
    fig, ax = plt.subplots(figsize=(5.5, 4))
    dx_vals = np.linspace(0.001, 2.0, 100)
    y_vals = (np.exp(dx_vals) - 1) / dx_vals
    dx_vals = np.insert(dx_vals, 0, 0.0)
    y_vals = np.insert(y_vals, 0, 1.0)
    ax.plot(dx_vals, y_vals, color='#546E7A', lw=2)
    ax.set_xlim(-0.1, 2.1)
    ax.set_ylim(0.8, 3.4)
    ax.set_xticks(np.arange(0, 2.25, 0.25))
    ax.set_yticks(np.arange(1.0, 3.5, 0.5))
    ax.grid(True, which='both', linestyle='-', linewidth=0.5, color='lightgray')
    ax.set_xlabel(r'$\Delta x$')
    ax.set_ylabel(r'$\frac{e^{\Delta x}-1}{\Delta x}$', rotation=0, labelpad=25, fontsize=12)
    plt.tight_layout()
    plt.savefig('fig5_exponential.png', dpi=300)
    plt.close()

    # 6. Product Rule Rectangle Diagram
    fig, ax = plt.subplots(figsize=(6, 5))
    u_x, v_x, du, dv = 3.0, 4.0, 1.0, 1.2
    rect_main = plt.Rectangle((0, du), v_x, u_x, facecolor='#E8EAF6', edgecolor='#4A3B8A', lw=2)
    ax.add_patch(rect_main)
    ax.add_patch(plt.Rectangle((v_x, du), dv, u_x, facecolor='none', edgecolor='black', linestyle=':', lw=1.5))
    ax.add_patch(plt.Rectangle((0, 0), v_x, du, facecolor='none', edgecolor='black', linestyle=':', lw=1.5))
    ax.add_patch(plt.Rectangle((v_x, 0), dv, du, facecolor='none', edgecolor='black', linestyle=':', lw=1.5))
    ax.text(v_x/2, du + u_x/2, r'$u(x) \cdot v(x)$', ha='center', va='center', fontsize=12, color='#4A3B8A')
    ax.text(v_x + dv/2, du + u_x/2, '1', ha='center', va='center', fontsize=12)
    ax.text(v_x/2, du/2, '2', ha='center', va='center', fontsize=12)
    #ax.text(v_x + dv/2, du/2, 'C', ha='center', va='center', fontsize=12)
    ax.annotate('', xy=(-0.3, du), xytext=(-0.3, du+u_x), arrowprops=dict(arrowstyle='<->', color='black'))
    ax.text(-0.4, du + u_x/2, r'$u(x)$', ha='right', va='center')
    #ax.annotate('', xy=(-0.7, 0), xytext=(-0.7, du+u_x), arrowprops=dict(arrowstyle='<->', color='black'))
    #ax.text(-0.8, (du + u_x)/2, r'$u(x+\Delta x)$', ha='right', va='center')
    ax.annotate('', xy=(0, du + u_x + 0.3), xytext=(v_x, du + u_x + 0.3), arrowprops=dict(arrowstyle='<->', color='black'))
    ax.text(v_x/2, du + u_x + 0.4, r'$v(x)$', ha='center', va='bottom')
    #ax.annotate('', xy=(0, du + u_x + 0.8), xytext=(v_x + dv, du + u_x + 0.8), arrowprops=dict(arrowstyle='<->', color='black'))
    #ax.text((v_x + dv)/2, du + u_x + 0.9, r'$v(x+\Delta x)$', ha='center', va='bottom')
    ax.annotate('', xy=(v_x, du + u_x + 0.3), xytext=(v_x + dv, du + u_x + 0.3), arrowprops=dict(arrowstyle='<->', color='black'))
    ax.text(v_x + dv/2, du + u_x + 0.4, r'$\Delta v$', ha='center', va='bottom')
    ax.annotate('', xy=(-0.3, 0), xytext=(-0.3, du), arrowprops=dict(arrowstyle='<->', color='black'))
    ax.text(-0.4, du/2, r'$\Delta u$', ha='right', va='center')
    ax.annotate('small, ignore', xy=(v_x + dv/2, du/2), xytext=(v_x + dv + 1.0, du/2),
                arrowprops=dict(arrowstyle='->', color='black', connectionstyle='arc3,rad=-0.2'), va='center')
    ax.text(v_x + dv + 0.2, du + u_x/2, r'Area 1 = $\Delta v \cdot u(x)$', va='center')
    ax.text(v_x/2 - 1.0, du/2 - 0.75, r'Area 2 = $\Delta u \cdot v(x)$', va='center')
    ax.set_xlim(-1.5, v_x + dv + 2.5)
    ax.set_ylim(-0.5, du + u_x + 1.5)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('fig6_product_rule.png', dpi=300)
    plt.close()

if __name__ == '__main__':
    generate_diagrams()
    print("All diagrams regenerated successfully.")
