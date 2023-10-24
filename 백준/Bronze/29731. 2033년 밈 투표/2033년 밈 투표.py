print('No' if all([{
                        'Never gonna give you up': 1, 
                        'Never gonna let you down': 1, 
                        'Never gonna run around and desert you': 1, 
                        'Never gonna make you cry': 1, 
                        'Never gonna say goodbye': 1, 
                        'Never gonna tell a lie and hurt you': 1, 
                        'Never gonna stop': 1}.get(input(),False) for _ in range(int(input()))]) else 'Yes')
