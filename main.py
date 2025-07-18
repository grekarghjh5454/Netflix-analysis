import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Чтение файла
df = pd.read_csv('Data/netflix_titles.csv')

# Проверка структуры
print(df.info())
print(df.head())

df = df.dropna(subset=['date_added'])

df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year

df['listed_in'] = df['listed_in'].fillna('Unknow')

print(df['type'].value_counts())

#Анализ фильмов и сериалов
content_by_year = df['year_added'].value_counts().sort_index()

#Дата когда был добавлен контент на сам нетфликс
plt.figure(figsize=(10,5))
sns.barplot(x=content_by_year.index, y=content_by_year.values, color="skyblue")
plt.title('Кол-во контента по годам добавления')
plt.xticks(rotation=45)
plt.xlabel('Год')
plt.ylabel("Количество")
plt.tight_layout()
plt.savefig("images/content_by_year.png")
plt.show()

#Анализ стран
top_countries = df['country'].value_counts().head(10)

plt.figure(figsize=(8,5))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('Топ 10 стран по количеству контента')
plt.xlabel('Количество')
plt.ylabel('Страна')
plt.tight_layout()
plt.savefig('images/top_countries.png')
plt.show()

#Анализ топ жанров
genre_counter = Counter()
for genres in df['listed_in']:
    for genre in genres.split(','):
        genre_counter[genre.strip()] += 1

top_genres = dict(sorted(genre_counter.items(), key=lambda x: x[1], reverse=True)[:10])

plt.figure(figsize=(8,5))
sns.barplot(x=list(top_genres.values()), y=list(top_genres.keys()), palette='coolwarm')
plt.title('Топ-10 жанров')
plt.xlabel('Количество')
plt.ylabel('Жанр')
plt.tight_layout()
plt.savefig('images/top_genres.png')
plt.show()     