class App:
    def __main__(self):
        if __name__ == "__main__":
            pass

    def __init__(self, prints):
        self.prints = print("Initializing Psych-Screen app...")
    


class Questionnaire:
    """
    This class sets up the format for any questionnaire-type form. Currently run only through terminal.
    Arguments are: head, prompts, answers
    """
    def __init__(self, head, prompts, answers):
        self.head = head
        self.prompts = prompts
        self.answers = answers
        #self.scores = scores
        #return super().__init__(prompt, answer)


def run_qstnr(q): 
    score = 0
    i = 0
    while i < len(q):
        print(q[i].head + q[i].prompts)
        ref = q[i].answers
        for lin in ref.values():
            print(lin)
        ans = input("\n Answer:  ")
        if ans == "Q":
            score = "*** ERROR: Incomplete ***"
            break
        else:
            try:
                ans = int(ans)
                ans in ref.keys()
                score += ans
                print("Your answer: {}".format(ref[ans][4:]))
                print("_"*50 + "\n")
                i+=1
            except:
                print("Answer not recognized...please try again...")
                print("_"*50 + "\n")
    return score
