  
  def validate_nft_actions(actions):
    if len(actions) % 2 == 1:
    	return False
    
    ele = 0  
    for action in actions:
    	if action == "add":
      	ele += 1
      elif action == "remove":
      	if ele <= 0:
        	return False
      	ele -= 1
        
    return ele == 0
