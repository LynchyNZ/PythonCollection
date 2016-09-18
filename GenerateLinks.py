''' Generates a list of links, start must be greater than finish, this is
    because we work our way from start to finish eg. from 100 to 0.'''

def GenerateLinks(start, finish):
    if start <= finish:
        print("Start must be greater than finish")
    else:
        current = start
        links = []
        while current > finish:
            print("<div class='swiper-slide'><img src='images/" + str(current).zfill(4) + ".jpg' alt='" + str(current).zfill(4) + "'></div>")
            current -= 1
    return "<!-- Linked generated by Lynchy's python script :) -->"


print(GenerateLinks(309, 0))

