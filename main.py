print(r"""
                        /\
                        ||
                        ||
                        ||
                        ||                                               ~-----~
                        ||                                            /===--  ---~~~
                        ||                   ;'                 /==~- --   -    ---~~~
                        ||                (/ ('              /=----         ~~_  --(  '
                        ||             ' / ;'             /=----               \__~
     '                ~==_=~          '('             ~-~~      ~~~~        ~~~--\~'
     \\                (c_\_        .i.             /~--    ~~~--   -~     (     '
      `\               (}| /       / : \           / ~~------~     ~~\   (
      \ '               ||/ \      |===|          /~/             ~~~ \ \(
      ``~\              ~~\  )~.~_ >._.< _~-~     |`_          ~~-~     )\
       '-~                 {  /  ) \___/ (   \   |` ` _       ~~         '
       \ -~\                -<__/  -   -  L~ -;   \\    \ _ _/
       `` ~~=\                  {    :    }\ ,\    ||   _ :(
        \  ~~=\__                \ _/ \_ /  )  } _//   ( `|'
        ``    , ~\--~=\           \     /  / _/ / '    (   '
         \`    } ~ ~~ -~=\   _~_  / \ / \ )^ ( // :_  / '
         |    ,          _~-'   '~~__-_  / - |/     \ (
          \  ,_--_     _/              \_'---', -~ .   \
           )/      /\ / /\   ,~,         \__ _}     \_  "~_
           ,      { ( _ )'} ~ - \_    ~\  (-:-)       "\   ~ 
                  /'' ''  )~ \~_ ~\   )->  \ :|    _,       " 
                 (\  _/)''} | \~_ ~  /~(   | :)   /          }
                <``  >;,,/  )= \~__ {{{ '  \ =(  ,   ,       ;
               {o_o }_/     |v  '~__  _    )-v|  "  :       ,"
               {/"\_)       {_/'  \~__ ~\_ \\_} '  {        /~\
               ,/!          '_/    '~__ _-~ \_' :  '      ,"  ~ 
              (''`                  /,'~___~    | /     ,"  \ ~' 
             '/, )                 (-)  '~____~";     ,"     , }
           /,')                    / \         /  ,~-"       '~'
       (  ''/                     / ( '       /  /          '~'
    ~ ~  ,, /) ,                 (/( \)      ( -)          /~'
  (  ~~ )`  ~}                   '  \)'     _/ /           ~'
 { |) /`,--.(  }'                    '     (  /          /~'
(` ~ ( c|~~| `}   )                        '/:\         ,'
 ~ )/``) )) '|),                          (/ | \)                 
  (` (-~(( `~`'  )                        ' (/ '
   `~'    )'`')                              '
     ` ``
""")
print("Welcome to Dragon Island.")
print("Your mission is to find the treasure.") 

#Write your code below this line 👇
first = input("Do you want to stay on the boat or get of it? \nStay or Get of \n")
first_lower = first.lower()
if first_lower == "stay":
  print("A kraken came out of the water and sink the ship with you on it. \nGame Over")
  print(r'''                        ___
                     .-'   `'.
                    /         \
                    |         ;
                    |         |           ___.--,
           _.._     |0) ~ (0) |    _.---'`__.-( (_.
    __.--'`_.. '.__.\    '--. \_.-' ,.--'`     `""`
   ( ,.--'`   ',__ /./;   ;, '.__.'`    __
   _`) )  .---.__.' / |   |\   \__..--""  """--.,_
  `---' .'.''-._.-'`_./  /\ '.  \ _.-~~~````~~~-._`-.__.'
        | |  .' _.-' |  |  \  \  '.               `~---`
         \ \/ .'     \  \   '. '-._)
          \/ /        \  \    `=.__`~-.
          / /\         `) )    / / `"".`\
    , _.-'.'\ \        / /    ( (     / /
     `--~`   ) )    .-'.'      '.'.  | (
            (/`    ( (`          ) )  '-;
             `      '-;         (-'
''')
else:
  print("You got of the boat and followed the beach until you felt like someone was watching you. ")
  print(r'''                     %%%%
                    %%%%-(
                  _%%%%%_/                        \ ' /
                _%%%%%%%%                        - (_) -
              _%%%%%%%/ \%                        / , \
             %%%%%%%%%\\ \_
               %%%%%%   \ \\
                   )    /\_/
                 /(___. \
                 '----' (
                /       )
    ---....____/        (_____ __ _ ___ ___ __ _ _ _____ _ _ ___
              /         )---...___ =-= = -_= -=_= _-=_-_ -=- =-_
            ,'          (         ```--.._= -_= -_= _-=- -_= _=-
         ,-'            )                 ``--._=-_ =-=_-= _-= _
         '-._    '-..___(                       ``-._=_-=_- =_-=
             ``---....__)                            `-._-=_-_=-
                   )|)|                                  `-._=-_
                  '-'-.\_                                    `-.
''')
  second = input("Do you want to rest on the beach or get into the forest? \nRest or Get into the forest \n")
  second_lower = second.lower()
  if second_lower == "rest":
    print("You were sitting under a palm tree when you suddenly felt a sharp pain! \n It looks like you've been stabed \n Game over")
    print(r''' ▬▬ι═══════>''')
  else:
    print(r'''            .        +          .      .          .
     .            _        .                    .
  ,              /;-._,-.____        ,-----.__
 ((        .    (_:#::_.:::. `-._   /:, /-._, `._,
  `                 \   _|`"=:_::.`.);  \ __/ /
                      ,    `./  \:. `.   )==-'  .
    .      ., ,-=-.  ,\, +#./`   \:.  / /           .
.           \/:/`-' , ,\ '` ` `   ): , /_  -o
       .    /:+- - + +- : :- + + -:'  /(o-) \)     .
  .      ,=':  \    ` `/` ' , , ,:' `'--".--"---._/`7
   `.   (    \: \,-._` ` + '\, ,"   _,--._,---":.__/
              \:  `  X` _| _,\/'   .-'
.               ":._:`\____  /:'  /      .           .
                    \::.  :\/:'  /              +
   .                 `.:.  /:'  }      .
           .           ):_(:;   \           .
                      /:. _/ ,  |
                   . (|::.     ,`                  .
     .                |::.    {\
                      |::.\  \ `.
                      |:::(\    |
              O       |:::/{ }  |                  (o
               )  ___/#\::`/ (O "==._____   O, (O  /`
          ~~~w/w~"~~,\` `:/,-(~`"~~~~~~~~"~o~\~/~w|/~
      ~~~~~~~~~~~~~~~~~~~~~~~\\W~~~~~~~~~~~~\|/~~''')
    print("The forest seems mysterious, there is a track on the ground, like people have already gone through here before \nMaybe we are on right path \nThe track seems to go left but there is an entrance to a cave on the right")
    third = input("Do you want to go left or right? \nLeft or Right ")
    third_lower = third.lower()
    if third_lower == "left":
      print("The cavern collapsed on you\n Game Over")
      print(r'''                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`

''')
    else:
      tracks = input("You found huge footprints on the track, \nWhat could've possibly make those? \n")
      print(f"You think there is no way {tracks} are on this island, do they even exist? \nAnyway you should get going")
      print("You stumbled into a wall, it seems to have three diferend colored rocks on the top of a sculpture")
      final = input("This seems like a treasure chamber doesn't it? \nMaybe if you press the right rock it will open \n Which rock should you press? \nRed, Green or Blue? \n")
      final_lower = final.lower()
      if final_lower == "red":
        print("Fire rained from the sky, you exclamed 'Oh it seems there was a Dragon after all' while burning into ashes \nGame Over")
        print(r'''                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`

''')
      elif final_lower == "green":
        print("A bright light shined through the rock and a the wall started opening, just like a door, you realize the cavern is full of chests with gold coins")
        print("Congratulations, You've found the treasure")
        print(r'''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
                '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
      else:
        print("You heard a noise coming from the wall, it started vibrating and colapsing on itself, it seems like we'll never know if there was a treasure there after all")
        print("To be continued...")
        print(r'''                  ___                           
               .dSSSS$$pp..                     
             .dSSSS$$$$$$$$;                    
           .dSSSS$$$$$$$$$$$                    
          :SSP^" T$$$$$$$$$$b_                  
         dSSP     $$$S$$$$$$$b`                 
        dSS$;_.  .:$$$SS$$$$$$b                 
       dSS$$$_ ;  __."^TSS$$$$$b                
      dSS$$P;"    ""'  :lSS$$$$$b               
     :SS$$$ ;          ::SS$$$$$$b_.            
     SSS$$$ :  `       ;:SS$$$$$$$bp.           
    :SS$$$$b \ -=-  .-" SSS$$$$$$$$$$b          
    SSS$$$$$b.`.   /   d$SS$$$$$$$$$$$b         
    :SS$$$$$$$; ""T   :$$$SS$$$$$$$$P^^t--'     
     SSS$$$S$$$   :   $$$$$SS$$$$$$$   :        
     :SS$$$SS$; __;  _$$$$$$SS$$$$$$   :        
      SSS$SS l;:  ;  :  $$$$SS$$$$$;   ;        
      :SS$SS $;:  ;  :  $$$SS$$$$$$;  /;        
       TSSSS :$ \ ;  ;  :$S$$$$$$$$.-"/         
        `SP; :;  ;:  ;   T$$$$$$$$;  /;         
         : ;  ;  : `.;   /)T$$$$$P .' :         
         ; :  :   ;    .'/ :$$$P'.'  .'\        
         ;  \    :;   /   /$P^".' .-"   ;       
         :       ;:     .'  .-"        / \      
          `.____/_'.___:--""\    --' .'   )     
        .-"      .'     "-._ "-._   ..--"")\    
       :-'      :     "-.   "-._    ---""" /;   
       ;    :   :        \      "-._....____;   
      :  :   \  :\        `.                 \  
      ;  ;    \  \\   \     \                 ; 
     :  :      `. \\   \     \                : 
     ;  ;       ;"-t\   `.    \               : 
    :  :       :    `;         \              ; 
    ;  ;       ;     :          \            /  
   :  :       /       ;          \-..__    .';  
   :  ;      /        :           ;    """T  ;  
   : /      /          ; \        :       ;  ;  
   ;/      :           :  \        ;      ;  ;  
   ;       ;            ;  ;       :      ;  ;  
  /       :             :  :        ;     ;  ;  
 /        ;             :;          :     ;  ;  
/        :              ::           ;    ;  ;_ 
`""--..__;              :_;      __  ;____;.-;';
   ;.__.:                 :..t-""  j"       ;  ;
   :    ;                 ;   ;--"" \       ;  ;
   ;    :                 ;   :      \      ;  ;
   :     \                ;    ;      ;.    ;  ;
    \     \               ;    :     /  ;   ;  ;
     \     \              ;    :        ;   ;  ;
      \     `-.           ;    ;      .'    ;  ;
       \       \          ;___/      /______;.-'
        \    ---;            /      /           
         ;______:         .-'      /            
                          '-------'             
''')
      
      
