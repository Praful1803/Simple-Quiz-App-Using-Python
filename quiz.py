quiz = {
  "question1": {
    "question": "what is the capital of india ?",
    "answer": "delhi"
  },
  "question2":{
    "question": "what is the capital of uttarakhand ?",
    "answer": "dehradun"
  },
    "question3":{
    "question": "what is the capital of united states ?",
    "answer": "washington"
  },
      "question4": {
    "question": "what is the capital of china ?",
    "answer": "beijing"
  },
  "question5":{
    "question": "what is the capital of germany ?",
    "answer": "italy"
  },
    "question6":{
    "question": "what is the capital of pakistan ?",
    "answer": "lahore"
  }
}

score = 0

for key, value in quiz.items():
  print(value['question'])
  answer = input("enter answer ?")
  
  if(answer.lower() == value['answer'].lower()):
    print("Correct!")
    score += 1
    print(f'your score is {score}!')
    print("")
    print("")
  
  else:
    print('Wrong')
    print('the correct answer is : ' + value['answer'])
    print(f'your score is {score}')
    print('')
    print('')
    
print(f'You got {score} out of 6 questions correctly')
print("Your percentage is " + str(int(score/6 * 100)) + "%")
