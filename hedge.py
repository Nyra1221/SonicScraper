import google, random, sys, webbrowser, os

def search():
    print "\n"
    query = raw_input("Enter a name: ") + "the hedgehog"
    if query == "!exit":
        sys.exit()
    elif query == "!rs":
        search()

    print "Searching..."

        
    ayylmao = google.search(query, tld='com', lang='en', num=10, start=0, stop=10, pause=2.0)
    print "\n"
    for thing in ayylmao:
        if "deviantart" in thing or "wikia" in thing:
            print thing + "\n" + "DANGER: YOUR MENTAL STABILITY CANNOT BE GUARANTEED BEYOND THIS POINT" + "\n"
            print "= = = = = = = = = = = = = = = = = = = = = = = = = ="
            stopthisnow = raw_input("Do you wish to disgrace yourself and view this? y/n ")
            print "= = = = = = = = = = = = = = = = = = = = = = = = = = " + "\n"

            if stopthisnow == "y":
                webbrowser.open(thing)
            elif stopthisnow == "!exit":
                sys.exit()
            elif stopthisnow == "!rs":
                os.execl(sys.executable, sys.executable, *sys.argv)
            else:
                continue
        else:
            print thing + "\n" "You're safe.. For now."
            print " = = = = = = = = = = = = = = = = = =" + "\n"

def rand():
    print "\n"
    names = open("names.txt", "r").read().splitlines()
    n = []
    for line in names:
        n.append(line)
        index = random.randint(0, len(n)-1)
        name = n[index] + " " + "the hedgehog"

    print "Name selected: {}".format(name)
    print "\n Searching..."


    ayylmao = google.search(name, tld='com', lang='en', num=10, start=0, stop=10, pause=2.0)
    for thing in ayylmao:
        if "deviantart" in thing:
            print thing + "\n" + "DANGER: YOUR MENTAL STABILITY CANNOT BE GUARANTEED BEYOND THIS POINT" + "\n"
            print "= = = = = = = = = = = = = = = = = = = = = = = = = ="
            stopthisnow = raw_input("Do you wish to disgrace yourself and view this? y/n ")
            print "= = = = = = = = = = = = = = = = = = = = = = = = = =" + "\n"

            if stopthisnow == "y":
                webbrowser.open(thing)
            elif stopthisnow == "!exit":
                sys.exit()
            elif stopthisnow == "!rs":
                os.execl(sys.executable, sys.executable, *sys.argv)
                
            else:
                continue
        else:
            print thing + "\n" "You're safe.. For now."
            print "= = = = = = = = = = = = = = = = = = = = =" + "\n"