#!/usr/bin/env python3
"""Fractal generator — Mandelbrot, Julia, Sierpinski, Koch."""
import sys

def mandelbrot(w=80, h=30, max_iter=50, xmin=-2.5, xmax=1, ymin=-1.2, ymax=1.2):
    chars = " .:-=+*#%@█"
    for row in range(h):
        line = ""
        for col in range(w):
            x0 = xmin + (xmax-xmin) * col / w
            y0 = ymin + (ymax-ymin) * row / h
            x, y, i = 0, 0, 0
            while x*x + y*y <= 4 and i < max_iter:
                x, y = x*x - y*y + x0, 2*x*y + y0
                i += 1
            line += chars[i * (len(chars)-1) // max_iter]
        print(line)

def julia(w=80, h=30, cx=-0.7, cy=0.27015, max_iter=50):
    chars = " .:-=+*#%@█"
    for row in range(h):
        line = ""
        for col in range(w):
            x = -2 + 4 * col / w
            y = -1.5 + 3 * row / h
            i = 0
            while x*x + y*y <= 4 and i < max_iter:
                x, y = x*x - y*y + cx, 2*x*y + cy
                i += 1
            line += chars[i * (len(chars)-1) // max_iter]
        print(line)

def sierpinski(n=5):
    size = 2**n
    for y in range(size):
        row = " " * (size - y - 1)
        for x in range(y + 1):
            row += "█ " if (x & y) == x else "  "
        print(row)

def koch_snowflake(depth=4, size=80):
    import math
    points = []
    def koch(x1, y1, x2, y2, d):
        if d == 0:
            points.append((x1, y1))
            return
        dx, dy = (x2-x1)/3, (y2-y1)/3
        ax, ay = x1+dx, y1+dy
        bx, by = x1+2*dx, y1+2*dy
        mx = (ax+bx)/2 - math.sqrt(3)/2*(by-ay)
        my = (ay+by)/2 + math.sqrt(3)/2*(bx-ax)
        koch(x1, y1, ax, ay, d-1); koch(ax, ay, mx, my, d-1)
        koch(mx, my, bx, by, d-1); koch(bx, by, x2, y2, d-1)
    s = size; h = s * math.sqrt(3) / 2
    koch(0, h, s, h, depth); koch(s, h, s/2, 0, depth); koch(s/2, 0, 0, h, depth)
    grid = {}
    for x, y in points:
        grid[(int(x), int(y*0.5))] = True
    if grid:
        ys = sorted(set(y for _, y in grid)); xs = sorted(set(x for x, _ in grid))
        for y in ys:
            print("".join("*" if (x, y) in grid else " " for x in range(max(xs)+1)))

if __name__ == "__main__":
    kind = sys.argv[1] if len(sys.argv) > 1 else "mandelbrot"
    if kind == "mandelbrot": mandelbrot()
    elif kind == "julia": julia()
    elif kind == "sierpinski": sierpinski()
    elif kind == "koch": koch_snowflake()
    else: print(f"Unknown: {kind}. Try: mandelbrot julia sierpinski koch")
