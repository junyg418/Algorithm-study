'''
단축키 지정(1283)s2
2022-07-24
1.실패 - NameError
사유:
    두번째 조건중 success 변수의 스코프가 for문 내에서 끝나
    for문 밖에 있는 success 를 참조하지 못하여 에러 발생
2. 성공
'''
word_count = int(input())
key_value = list()
for _ in range(word_count):
    word = input().split()
    breaker = False
    # 첫번쨰 조건 - 단어단위 첫글자
    for idx, first_vals in enumerate(word):
        first_val = first_vals[0]

        if first_val.upper() not in key_value:
            key_value.append(first_val.upper())
            # key_idx = ' '.join(word).index(first_val)
            # value = ' '.join(word)
            # answer = value[:key_idx] + '[' + value[key_idx] + ']' + value[key_idx+1:]
            word[idx] = '[' + word[idx][0] + ']' + word[idx][1:]
            answer = ' '.join(word)
            breaker = True
            print(answer)
            break
    if breaker:
        continue
    else:
        # 두번째 조건 - 모든 단어, 글자단뒤 
        for word_idx, second_keys in enumerate(word):
            success = False
            for alpa_idx, alpa in enumerate(second_keys):
                if alpa.upper() not in key_value:
                    word[word_idx] = word[word_idx][:alpa_idx] + '[' + word[word_idx][alpa_idx] + ']' + word[word_idx][alpa_idx+1:]
                    print(' '.join(word))
                    key_value.append(alpa.upper())
                    success = True
                    breaker = True
                    break

            if success:
                break
    if breaker:
        continue
    print(' '.join(word))   
                