# NKiteDB

**NKiteDB** is a lightweight and flexible NoSQL database library that uses a JSON file for data storage. It provides simple CRUD (Create, Read, Update, Delete) operations and makes it easy to manage your data collections.

## Features

- **File-Based Storage:** Data is stored in a specified JSON file.
- **Collection Support:** Organize different datasets into collections.
- **CRUD Operations:** Perform basic database operations using `insert`, `find`, `get_first`, `update`, `delete`, and `get_all` methods.
- **Ease of Use:** Its simple interface allows for easy integration into your projects.

## Installation

NKiteDB relies only on Python's built-in `json` and `os` modules. No additional installation is required. Simply include the `NKiteDB` class in your project or clone this repository.

```bash
git clone https://github.com/Leo4Bey/NKiteDB/
pip install NKiteDB
```


**NKiteDB**, JSON dosyası kullanarak veri saklayan, hafif ve esnek bir NoSQL veritabanı kütüphanesidir. Basit CRUD (Create, Read, Update, Delete) işlemleri sunar ve veri koleksiyonlarını kolayca yönetmenizi sağlar.

## Özellikler

- **Dosya Tabanlı Depolama:** Veriler, belirtilen bir JSON dosyasında saklanır.
- **Koleksiyon Desteği:** Farklı veri kümelerini koleksiyonlar halinde organize edebilirsiniz.
- **CRUD İşlemleri:** `insert`, `find`, `get_first`, `update`, `delete` ve `get_all` metodları ile temel veritabanı işlemleri gerçekleştirin.
- **Kolay Kullanım:** Basit arayüzü sayesinde projelerinize kolayca entegre edilebilir.

## Kurulum

NKiteDB, bağımlılık olarak yalnızca Python'un yerleşik `json` ve `os` modüllerini kullanır. Ekstra bir kurulum yapmanıza gerek yoktur. Sadece `NKiteDB` sınıfını projenize dahil edin veya bu repoyu klonlayın.

```bash
git clone https://github.com/Leo4Bey/NKiteDB/
pip install NKiteDB
```


## Usage / Kullanım

The following example demonstrates how to perform basic CRUD (Create, Read, Update, Delete) operations with NKiteDB. / Aşağıdaki örnek kod, NKiteDB ile temel CRUD (Create, Read, Update, Delete) işlemlerini nasıl gerçekleştireceğinizi gösterir.

```python
from nkitedb import NKiteDB 

# 1. Initialize the Database / Veritabanını Başlatma
# If the specified JSON file does not exist, NKiteDB will automatically create an empty file.
# Eğer belirtilen JSON dosyası yoksa, NKiteDB otomatik olarak boş bir dosya oluşturacaktır.
db = NKiteDB("nkdatabase.json")

# 2. Insert Data (Add New Documents) / Veri Ekleme (Yeni Belgeler Ekleme)
# Insert two user documents into the "users" collection.
# "users" koleksiyonuna iki adet kullanıcı belgesi ekleyelim.
db.insert("users", {"id": 1, "name": "Kemal", "age": 20})
db.insert("users", {"id": 2, "name": "Nehir", "age": 19})

# 3. Find Data / Veri Arama
# Find all documents in the "users" collection where "name" is "Kemal".
# "name" alanı "Kemal" olan tüm belgeleri "users" koleksiyonunda arar.
results = db.find("users", {"name": "Kemal"})
print("Find results:", results)
print("Arama sonuçları:", results)

# 4. Get First Matching Document / İlk Eşleşen Belgeyi Alma
# Get the first document where "age" is 20.
# "age" alanı 20 olan ilk belgeyi getirir.
first_user = db.get_first("users", {"age": 20})
print("First user:", first_user)
print("İlk kullanıcı:", first_user)

# 5. Update Data / Veri Güncelleme
# Update the document where "name" is "Kemal" and set "age" to 21.
# "name" alanı "Kemal" olan kullanıcı belgesini bulup "age" değerini 21 olarak günceller.
updated = db.update("users", {"name": "Kemal"}, {"age": 21})
print("Update successful?", updated)
print("Güncelleme başarılı mı?", updated)

# 6. Delete Data / Veri Silme
# Delete the document where "id" is 1.
# "id" alanı 1 olan kullanıcı belgesini siler.
deleted = db.delete("users", {"id": 1})
print("Delete successful?", deleted)
print("Silme başarılı mı?", deleted)

# 7. Get All Documents / Tüm Belgeleri Alma
# Get all documents from the "users" collection.
# "users" koleksiyonundaki tüm belgeleri getirir.
all_users = db.get_all("users")
print("All users:", all_users)
print("Tüm kullanıcılar:", all_users)
