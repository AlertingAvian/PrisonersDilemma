name = 'Team 4'
plan = 'Try to actually win'

from randcrack import RandCrack
import random
rc = RandCrack()


def action(iteration,opponent_history):
  '''This is where the execution of your plan will go. '''
  go = False
  reactions = {'a':'b','b':'b','c':'b'}
  if iteration == 0:
    go = True
  predicted = guess(go)
  return reactions[predicted]
  
def guess(go):
  if go:
    for i in range(624):
      rc.submit(random.getrandbits(32))
  return rc.predict_choice(['a','c','b'])

