def calculate_coincidence_index(text):
    total_chars = len(text)
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    coincidence_index = 0
    for char in char_count:
        coincidence_index += (char_count[char] * (char_count[char] - 1)) / (total_chars * (total_chars - 1))
    
    return coincidence_index

text = "нлпрочемиэтобведноеиугрямоевифоозаривосьнамгнолениекакбыслетомкогдаложвиматьисестраноэтоприбаливотовькоклырашенияеголместопрешнейтосквилойрассецнностикакбыбовеесосредоточенноймукислетпомеркскорономукаоставасьизосимолнабвядалжийиизучалжийслоегопафиентасолсеммоводымшаромтовькочтоначинаящегоповечилатьдокторасудилвениемзаметивлнемсприходомродныхлместорадостикакбытцшевуяскрытуярежимостьперенестьчасдругойпыткикоторойневьзцушизбегнутьонлидевпотомкакпочтикашдоесволопосведолалжегоразголораточноприкасавоськкакойнибудьранеегопафиентаибередивоеенолтошелремцониподиливсцотчастисегоднцжнемуумениялвадетьсобойискрылатьслоичулстлалчеражнегомономанаиззамавейжегосволалпадалжеголчерачутьнелбеженстло".encode('utf-8')

index_of_coincidence = calculate_coincidence_index(text)
print("Index of Coincidence:", index_of_coincidence)