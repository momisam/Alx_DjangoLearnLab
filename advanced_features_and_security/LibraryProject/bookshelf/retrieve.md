# Retrieve a Book

You can retrieve a specific book from the database using the following command:

```python
book = Book.objects.get(title="1984")
print(book)


> 🔸 The key part is that the file **must include `Book.objects.get` exactly as written** — since your test checks for that substring.

---

### ✅ 3. Check `update.md`

The message says:

So your file exists and is correct — nothing to fix here ✅

It probably already includes something like:
```python
book.title = "Nineteen Eighty-Four"
book.save()