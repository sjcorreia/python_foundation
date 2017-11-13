from __future__ import print_function
import time
import webbrowser

total_breaks = 3
break_count = 0
sleep_time = 2

print("This program started on "+time.ctime())

while(break_count < total_breaks):
                time.sleep(sleep_time)
                # webbrowser.open("https://www.youtube.com/watch?v=DHkbhQC1hDc&t=630s")
                print("Take a break!!")
                break_count += 1

print(__module__)