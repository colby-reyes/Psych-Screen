class App:
    def __main__():
        if __name__ == "__main__":
            pass

    def __init__():
        print("Initializing Psych-Screen app...")

class Questionnaire:
    def __init__(self, head, prompts, answers, scores):
        self.head = head
        self.prompts = prompts
        self.answers = answers
        self.scores = scores
        #return super().__init__(prompt, answer)

header="Over the past 2 weeks, how often have you been bothered by...\n"
opts = ["0","1","2","3"]
dispOpts = [
    "0 - Not at all",
    "1 - Several days",
    "2 - More than half the days",
    "3 - Nearly every day"
]

phq_prompts = [
    Questionnaire(header, "Little interest or pleasure in doing things", dispOpts, opts),
    Questionnaire(header, "Feeling down, depressed, or hopeless", dispOpts, opts),
    Questionnaire(header, "Trouble falling asleep or staying asleep, or sleeping too much", dispOpts, opts),
    Questionnaire(header, "Feeling tired or having little energy", dispOpts, opts),
    Questionnaire(header, "Poor appetite or overeating", dispOpts, opts),
    Questionnaire(header, "Feeling bad about yourself; feeling that you are a failure or that you have let yourself or your family down", dispOpts, opts),
    Questionnaire(header, "Trouble concentrating on things (such as reading the newspaper or watching TV", dispOpts, opts),
    Questionnaire(header, "Moving or speaking so slowly that other people could have noticed. Or the opposite - being so fidgety or restless that you have been moving around a lot more than usual", dispOpts, opts),
    Questionnaire(header, "Thoughts that you would be better off dead, or of hurting yourself", dispOpts, opts)
]


endOpts = [
"0 - Not difficult at all",
"1 - Somewhat difficult",
"2 - Very difficult",
"3 - Extremely difficult"
]

endQ = [Questionnaire(head="",prompts="If you checked off any problems, how difficult have these problems made it for you to do your work, take care of things at home, or get along with other people?",answers=endOpts,scores=opts)]


def run_qstnr(q): 
    score = 0
    i = 0
    while i < len(q):
        print(q[i].head + q[i].prompts)
        for lin in q[i].answers:
            print(lin)
        ans = input("\n Answer:  ")
        if ans in q[i].scores:
            score += int(ans)
            print("Your answer: {}".format(q[i].answers[int(ans)][4:]))
            print("_"*50 + "\n")
            i+=1
        else:
            print("Answer not recognized...please try again...")
            print("_"*50 + "\n")
    return score

score_now = run_qstnr(phq_prompts)
fin = run_qstnr(endQ)
dif = endOpts[fin]

print("Your PHQ-9 score today is: {}\nYou rated your level of difficulty as: {}".format(score_now,dif[4:]))