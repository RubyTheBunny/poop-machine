import time
import sys
import random

ascii_rabit = r'''
   ***
  ** **
 **   **
 **   **         ****
 **   **       **   ****
 **  **       *   **   **
  **  *      *  **  ***  **
   **  *    *  **     **  *
    ** **  ** **        **
    **   **  **
   *           *
  *             *
 *    0     0    *
 *   /   @   \   *
 *   \__/ \__/   *
   *     W     *
     **     **
       *****
'''

def make_poop():
  return random.randint(0, 3) * "."

def jump():
    timeline = ""
    for i in range(10):
        timeline += ( i * ' ') + make_poop()

    return timeline

jump_timeline = jump()
for i in range(len(jump_timeline)):
    time.sleep(0.1)
    sys.stdout.write("\r" + jump_timeline[0:i])
    sys.stdout.flush()

print ascii_rabit
print "Empty fuel. Feed me!"
