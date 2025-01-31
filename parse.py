from html.parser import HTMLParser

#timetable response parsing
def parse_timetable_response(url_response:list)->dict:
    timetables = {}
    
    for timetable in url_response:
        timetables[timetable["Title"]] = timetable["Childs"][0]["Detail"]

    return timetables


class TimetableHTMLParser(HTMLParser):
    def __init__(self, *, convert_charrefs = True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.tag_stack = []
        self.timetable_data = {}
        self.curr_timetable_element = ""
    
    def handle_starttag(self, tag, attrs):
        print(self.tag_stack)
        self.tag_stack.append(tag)
        match tag:
            case "table":
                match attrs[0][1]:
                    case "class":
                        pass
                            
            case "div":
                match attrs[0][1]:
                    case "class":
                        match attrs[0][2]:
                            case "mon_title":
                                self.curr_timetable_element = "date"
        

    def handle_endtag(self, tag):
        
        self.tag_stack.pop()

    def handle_data(self, data):
        match self.curr_timetable_element:
            case "date":
                self.timetable_data["date"] = data
        

    def get_timetable_data(self):
        return self.timetable_data