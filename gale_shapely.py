def stableMatching(n, mpref, wpref):
  wpart=['free']*n
  mpart=['free']*n
  count=n
  while count>0:
    #going through one man at a time 
    for man in range(n):
      #if the current man is free
      #print("this one goes for the man number ",man )
    
      if mpart[man]=='free':
        #going through the women in the mans preference list 
        for W in range(n):
          women=mpref[man][W]
          #print("the women in the man number ",man,"preference list is ",women)
          # here ive changed line 34 from wpart[W] -> wpart[women]
        
          if wpart[women]=='free':
            #print("women ",women, "is free for man number ",man )
            mpart[man]=women
            wpart[women]=man
            count=count-1
            #print(mpart,wpart)

            break
          else:
            #print("women ",women," is not free for ",man)
            man_old=wpart[women]
            #print(" her current partner is ",man_old)
            for m in range(n):
              #if the new man is prefered over the previous man
              if wpref[women][m]==man:
                #print(" this man ", man," is prefered over her current partner")
                mpart[man]=women
                mpart[man_old]='free'
                wpart[women]=man
                #print(mpart,wpart)
                b=1
                break

              #if the previous man is still prefered
              if wpref[women][m]==man_old:
                #print( "this man ",man," is not prefered over her current partner")
                mpart[man_old]=women
                mpart[man]='free'
                wpart[women]=man_old
                #print(mpart,wpart)
                break
          if b==1:
            b=0
            break
  return mpart
  

n=2
mpref=[[0,1],[0,1]]
wpref=[[1,0],[0,1]]
answer=stableMatching(n, mpref, wpref)
print(answer)
