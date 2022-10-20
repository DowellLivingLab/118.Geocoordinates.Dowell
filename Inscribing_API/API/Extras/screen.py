import tkinter as tk

import os
os.environ['DISPLAY'] = ':0'
os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'

root = tk.Tk()

width_px = root.winfo_screenwidth()
height_px = root.winfo_screenheight()
width_mm = root.winfo_screenmmwidth()
height_mm = root.winfo_screenmmheight()
# 2.54 cm = in
width_in = width_mm / 25.4
height_in = height_mm / 25.4
width_dpi = width_px/width_in
height_dpi = height_px/height_in

print('Width: %i px, Height: %i px' % (width_px, height_px))
print('Width: %i mm, Height: %i mm' % (width_mm, height_mm))
print('Width: %f in, Height: %f in' % (width_in, height_in))
print('Width: %f dpi, Height: %f dpi' % (width_dpi, height_dpi))