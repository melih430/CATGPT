
# app.py
# Tüm kedi bilgi kategorilerini içeren terminal tabanlı chatbot

CAT_KNOWLEDGE = {
    "ırklar": {
        "Sphynx": "Tüysüz kedidir. Çok sıcak ortam sever, oyuncu ve insana bağlıdır.",
        "Ragdoll": "Yumuşak mizaçlı, büyük bedenli, kucağı çok seven bir ırktır.",
        "Norwegian Forest Cat": "Yoğun tüylüdür, soğuğa dayanıklıdır, Norveç kökenlidir.",
        "Oriental Shorthair": "Siyam'a benzer, uzun kulaklı ve çok konuşkandır.",
        "Exotic Shorthair": "Pers'e benzer ama kısa tüylüdür. Sakin ve uykucu bir ırktır.",
    },
    "sağlık": {
        "diş hastalıkları": "Gingivit ve periodontal hastalıklar en sık görülen problemler arasındadır.",
        "kalıtsal hastalıklar": "Perslerde polikistik böbrek hastalığı (PKD) yaygındır.",
        "obezite": "Kısır kedilerde ve ev kedilerinde çok yaygındır. Diyetle kontrol edilmelidir.",
        "aşı takvimi": "İlk aşılar 6-8 haftalıkken başlar. Karma, FeLV, kuduz, iç-dış parazit aşıları sırasıyla yapılır.",
        "ilk yardım": "Zehirlenmede HEMEN veteriner aranmalı. Aktif kömür asla veterinersiz verilmemeli.",
    },
    "davranış": {
        "kuyruk dili": "Kuyruk dikse mutlu, kıpır kıpırsa heyecanlı, kabarıksa korkmuş demektir.",
        "kafa sürtme": "Sahibine koku bırakma, aidiyet belirtisidir.",
        "yuvarlanma": "Rahat hissetme, oyun daveti veya güven belirtisi.",
        "gizlenme": "Yeni ortamda veya hasta/rahatsız kedilerde yaygındır.",
        "titreme": "Soğuk, stres, düşük şeker, zehirlenme gibi nedenleri olabilir.",
    },
    "beslenme": {
        "laktoz intoleransı": "Süt çoğu kedide ishale neden olur. Yetişkin kedilere verilmemeli.",
        "balık": "Aşırı balık tüketimi B1 vitamini eksikliğine neden olabilir.",
        "çiğ yumurta": "Avidin içerdiği için Biyotin emilimini engeller. Çiğ verilmemeli.",
        "bitkisel gıdalar": "Kediler zorunlu etoburdur. Vejetaryen beslenemez.",
        "besin alerjisi": "Sık alerjenler: tavuk, balık, tahıl. Kaşıntı ve kulak problemleriyle kendini gösterir.",
    },
    "bakım": {
        "tırnak kesimi": "İç mekanda yaşayan kedilerin tırnakları 2-4 haftada bir kesilmelidir.",
        "kulak bakımı": "Kulağın içi kirliyse nemli pamukla silinir, kahverengi akıntı varsa mantar/pire olabilir.",
        "koku giderme": "Kedi kumu karbonatla desteklenebilir. Sprey kullanılmamalı.",
        "deri bakımı": "Kediler kendi tüylerini yutar; haftalık tarama tüy yumağı riskini azaltır.",
        "evde güvenlik": "Pencere filesi, kapalı çöp kutusu, tehlikeli bitkilerden arındırma şarttır.",
    },
    "yavru bakımı": {
        "annelik": "Anne kedi 6-8 haftalık olana dek yavrularla kalmalı. 4. haftada mama eklenir.",
        "sütten kesilme": "6-8 hafta arası tamamlanır. 1 yaşına kadar yavru maması verilmelidir.",
        "erken sosyalleşme": "İnsan sesi, oyuncak, kum ve mama ile 2. haftadan itibaren tanıştırılmalı.",
        "mikroçip": "Zorunlu değil ama önerilir. 8 haftadan sonra uygulanabilir.",
    },
    "yaşlı kediler": {
        "artrit": "Yaşlı kedilerde sık görülür. Merdiven çıkmama, zıplamama dikkat edilmelidir.",
        "böbrek yetmezliği": "12 yaş üstü kedilerde yaygındır. Yaş mama ve su tüketimi artırılmalı.",
        "mental değişimler": "Yaşlılıkla yön bulma problemi, miyavlama artışı olabilir.",
        "özel diyetler": "Böbrek, kalp veya eklem destekli veteriner mamaları önerilir.",
    },
    "genel bilgiler": {
        "üreme": "Dişi kediler 5-6 aylıkken kızgınlığa girer. Yılda birkaç kez olabilir.",
        "patiler": "Her pati parmak izi gibidir. Her kedide eşsizdir.",
        "ses çıkarma türleri": "Miyavlama, hırıltı, tıslama, mırlama, çığlık (kavga veya çiftleşme).",
        "ısı toleransı": "Sıcak havalarda çok etkilenirler. 28°C üzeri sıcaklık risklidir.",
        "soğuk toleransı": "Tüylü ırklar daha dayanıklıdır ama 10°C altına inmemeli.",
    },
    "halk arasındaki yanlışlar": {
        "süt verirsen iyi olur": "Hayır, çoğu kedi laktoz intoleranslıdır.",
        "kedi nankördür": "Hayır, sadece insan gibi davranmaz. Sahibini tanır, bağ kurar.",
        "hamilelikte kedi zararlıdır": "Toksoplazma sadece dışkıyla bulaşır. Kum temizliği önlemiyle risk sıfıra yakın.",
        "kedi kendi haline bırakılır": "Kediler yalnız kalmaktan sıkılır. Günde 15-30 dk ilgi ister.",
    },
    "acil durumlar": {
        "zehirlenme belirtileri": "Salya akması, kusma, titreme, yürüyememe. Hemen veteriner aranmalı.",
        "kedi yüksekten düştü": "Görünürde yara yoksa bile iç kanama olabilir. Geciktirmeden muayene edilmeli.",
        "idrar yapamama": "Acil bir durumdur, genellikle idrar tıkanıklığı. Erkek kedilerde ölümcüldür.",
        "kanlı dışkı": "İç parazit, zehirlenme, bağırsak hastalıkları gibi ciddi nedenlerle olabilir.",
    },
}

def list_categories():
    print("\nKategoriler:")
    for i, category in enumerate(CAT_KNOWLEDGE.keys(), 1):
        print(f"{i}. {category}")
    print()

def list_keywords(category):
    print(f"{category} kategorisindeki başlıklar:")
    for i, keyword in enumerate(CAT_KNOWLEDGE[category].keys(), 1):
        print(f"{i}. {keyword}")
    print()

def show_info(category, keyword):
    print(f"\n[{category.upper()}] {keyword}: {CAT_KNOWLEDGE[category][keyword]}\n")

def run_chatbot():
    while True:
        list_categories()
        selected_category = input("Bir kategori seçin (çıkmak için q): ")
        if selected_category.lower() == 'q':
            break

        try:
            category_name = list(CAT_KNOWLEDGE.keys())[int(selected_category) - 1]
        except:
            print("Geçersiz seçim.\n")
            continue

        list_keywords(category_name)
        selected_keyword = input("Bir başlık seçin (geri dönmek için b): ")
        if selected_keyword.lower() == 'b':
            continue

        try:
            keyword_name = list(CAT_KNOWLEDGE[category_name].keys())[int(selected_keyword) - 1]
            show_info(category_name, keyword_name)
        except:
            print("Geçersiz seçim.\n")

if __name__ == "__main__":
    run_chatbot()
