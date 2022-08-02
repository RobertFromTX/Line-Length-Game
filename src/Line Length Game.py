# Draws five lines then asks the user to choose the longest and shortest line.
# Must guess both the longest and shortest lines correct to win the game.

import turtle
import random

def origin(line):
    turtle.penup()
    turtle.setpos(-869, 521- (line * 200))
    turtle.pendown()

# the procedure below generates one line with random numbers each time it is # called upon
def make_line():
    turns = random.randint(10, 20)
    turn_angle = random.randint(2,87)
    if turn_angle < 20:
        pass
    segment_lengths = random.randint(100,200)

#could make it check before makes the next move ****************************
    actual_turns = 0
    for x in range(0,turns):
        if x % 2 == 0 and turtle.pos()[0] < 800: #the second condition makes #sure line doesn't go off page
            turtle.setheading((turtle.heading()) - (turn_angle))
            turtle.forward(segment_lengths)
            turtle.setheading((turtle.heading()) + (turn_angle))
            actual_turns += 1
        if x % 2 == 1 and turtle.pos()[0] < 800:
            turtle.setheading((turtle.heading()) + (turn_angle))
            turtle.forward(segment_lengths)
            turtle.setheading((turtle.heading()) - (turn_angle))
            actual_turns += 1
    actual_length = segment_lengths * actual_turns
    return actual_length

# this procedure sorts the line lengths from shortest to longest and provides #the number of the line
def sort_list(length_list):
    sorted_list = length_list.copy()
#first part: sorts the line lengths from shortest to longest
    for x in range(len(sorted_list)):
        temp = sorted_list[x]
        min = sorted_list[x]
        flag = False
        for y in range(x, len(sorted_list)):
            if sorted_list[y] < min:
                min = sorted_list[y]
                y_switch = y
                flag = True
        if flag == True:
            sorted_list[x] = min
            sorted_list[y_switch] = temp

#second part: creates list of the line numbers sorted by the length of their #lines
    tie = 0
    answer_key = [] #creates list with line numbers from shortest to longest #lines
    for length in sorted_list:
        for index in range(len(length_list)):
            if length_list[index] == length:
                if not((index+1) in answer_key):
                    answer_key.append(index+1)
                    break
                elif((index+1) in answer_key):
                    tie = 1
    return sorted_list, answer_key, tie

#setup
turtle.screensize(4000, 4000)
turtle.setup(width = 1.0, height = 1.0)
turtle.shape("turtle")
turtle.shapesize(2, 2, 1)
window:object = turtle.Screen()
turtle.speed(69)

#MAIN()
line_lengths = []
for x in range(5): # this loop creates 5 lines and records the total length #of each line
    origin(x)
    print("Making line", str(x + 1) + "...")
    order = make_line()
    line_lengths.append(order)
print("")

# sorted_lengths is a list of line lengths from shortest to longest
sorted_lengths = sort_list(line_lengths)[0]
# sorted_line_nums is a list of the line numbers of the line lengths organized shortest to longest
sorted_line_nums = sort_list(line_lengths)[1]
longest_lines = [sorted_line_nums[4]]
shortest_lines = [sorted_line_nums[0]]

# in case there is a tie in the shortest or longest line
if (sort_list(line_lengths)[2]) == 1:
    print("Ties: yes")
    for lines in range(4):
        if line_lengths[lines] == sorted_lengths[4] and (lines+1) not in longest_lines:
            longest_lines.append(lines+1)
    for lines in range(4):
        if line_lengths[lines] == sorted_lengths[0] and (lines+1) not in shortest_lines:
            shortest_lines.append(lines+1)
else:
    print("Ties: no")

# this part asks the questions
print("\nQuestions:")
long_input = int(input("1. Which line (1-5) was the longest? ")) #must input #integer 1-5
short_input = int(input("2. Which line (1-5) was the shortest? ")) #must #input integer 1-5
print("")

# the score starts off as zero
score = 0

# a point is gained for each question correct
if long_input in longest_lines:
    score += 1
print("Longest line(s):")
for line_num in longest_lines:
    print("Line", line_num)
if short_input in shortest_lines:
    score += 1
print("Shortest line(s):")
for line_num in shortest_lines:
    print("Line", line_num)

# prints results of game
if score == 2: # need score of two to win
    print("\nYou Win!")
else:
    print("\nYou Lose!")
print("\nLine lengths:")
print("  1  |  2  |  3  |  4  |  5  ")
print(line_lengths)


window.exitonclick()

