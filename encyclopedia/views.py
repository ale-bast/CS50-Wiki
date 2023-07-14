from django.shortcuts import render, redirect
from django.urls import reverse
from . import util
import random
import markdown2


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry_content = util.get_entry(title)
    if entry_content:
        html_content = markdown2.markdown(entry_content)
        return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": html_content
        })
    else:
        return render(request, "encyclopedia/error.html", {
        "error_message": "Page not found"
        })

def search(request):
    query = request.GET.get("q", "")
    entry_content = util.get_entry(query)

    if entry_content:
        return redirect(reverse("entry", args=[query]))
    else:
        entries = util.list_entries()
        search_results = []
        search_results = [entry for entry in entries if query.lower() in entry.lower()]
        if search_results:
            return render(request, "encyclopedia/search.html", {
                "query": query,
                "search_results": search_results
            })
        else:
            return render(request, "encyclopedia/error.html", {
            "error_message": "No search results"
            })

def create(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")

        if not title or not content:
            return render(request, "encyclopedia/create.html", {
                "error_message": "Title and content are required.",
                "title_value": title,
                "content_value": content
            })

        if util.get_entry(title):
            return render(request, "encyclopedia/create.html", {
                "error_message": "An entry with the same title already exists.",
                "title_value": title,
                "content_value": content
            })

        util.save_entry(title, content)
        return redirect(reverse("entry", args=[title]))
    else:
        return render(request, "encyclopedia/create.html")

def edit(request, title):
    if request.method == "POST":
        content = request.POST.get("content", "")

        util.save_entry(title, content)
        return redirect(reverse("entry", args=[title]))
    else:
        entry_content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content_value": entry_content
        })

def random_page(request):
    entries = util.list_entries()
    if entries:
        random_title = random.choice(entries)
        return redirect(reverse("entry", args=[random_title]))
    else:
        return render(request, "encyclopedia/error.html", {
            "error_message": "No encyclopedia entries found."
        })