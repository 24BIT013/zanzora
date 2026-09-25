from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Inquiry, TransportRequest

TOURS = [
    {"slug": "serengeti-soul", "title": "Serengeti Soul Safari", "place": "Northern Tanzania", "days": 6, "price": 2480, "rating": "4.9", "tag": "Wildlife", "image": "https://images.unsplash.com/photo-1516426122078-c23e76319801?auto=format&fit=crop&w=1200&q=85", "accent": "gold", "description": "Follow the great grasslands from the Ngorongoro highlands to the endless plains, with private camps and a naturalist guide."},
    {"slug": "spice-and-tide", "title": "Spice & Tide Escape", "place": "Zanzibar Archipelago", "days": 5, "price": 1790, "rating": "4.8", "tag": "Coast", "image": "https://images.unsplash.com/photo-1540202404-a2f29016b523?auto=format&fit=crop&w=1200&q=85", "accent": "coral", "description": "Stone Town stories, fragrant spice farms, and slow afternoons on turquoise Indian Ocean shores."},
    {"slug": "kilimanjaro-rhythm", "title": "Kilimanjaro Rhythm", "place": "Mount Kilimanjaro", "days": 8, "price": 3250, "rating": "5.0", "tag": "Adventure", "image": "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1200&q=85", "accent": "sage", "description": "A considered Machame route ascent with expert mountain support, acclimatisation days, and summit sunrise."},
    {"slug": "ruaha-untamed", "title": "Ruaha Untamed", "place": "Southern Tanzania", "days": 7, "price": 2860, "rating": "4.9", "tag": "Wildlife", "image": "https://images.unsplash.com/photo-1547970810-dc1eac37d174?auto=format&fit=crop&w=1200&q=85", "accent": "rust", "description": "Trade the crowds for elephant-rich river valleys, baobab silhouettes, and exceptional walking safaris."},
]
GALLERY = [
    {"image": "https://images.unsplash.com/photo-1510414842594-a61c69b5ae57?auto=format&fit=crop&w=1000&q=85", "title": "Dawn, Nungwi", "copy": "The sea turns from ink to glass before the village wakes. We love this quiet hour for a barefoot walk, a slow coffee, and the sense that the island belongs entirely to you."},
    {"image": "https://images.unsplash.com/photo-1530789253388-582c481c54b0?auto=format&fit=crop&w=1000&q=85", "title": "A spice farm afternoon", "copy": "Clove, cardamom and cinnamon—Zanzibar’s most fragrant welcome. Let a local grower show you the ingredients and stories hidden in every leaf."},
    {"image": "https://images.unsplash.com/photo-1500534623283-312aade485b7?auto=format&fit=crop&w=1000&q=85", "title": "Where the wild pauses", "copy": "A quiet encounter is often the one you remember longest. We leave space in every safari day for the unscripted, heart-stopping moments."},
]


def saved(request):
    return request.session.get("saved_tours", [])


def find_tour(slug):
    for tour in TOURS:
        if tour["slug"] == slug:
            return tour
    raise Http404("Journey not found")


def home(request):
    return render(request, "explore/home.html", {"tours": TOURS[:3], "saved_slugs": saved(request)})


def gallery(request):
    return render(request, "explore/gallery.html", {"gallery": GALLERY})


def zanzibar_stories(request):
    stories = [
        {"number": "01", "title": "Stone Town after rain", "copy": "Follow carved doorways and coffee-scented lanes with a storyteller who calls this place home."},
        {"number": "02", "title": "The art of a dhow sail", "copy": "Sail into a honey-coloured sunset on a traditional wooden dhow, with nothing urgent ahead."},
        {"number": "03", "title": "Tides that reveal worlds", "copy": "At low tide, the shoreline opens a path to sandbanks, coral gardens and a very long lunch."},
    ]
    return render(request, "explore/stories.html", {"stories": stories})


def plan_trip(request):
    return render(request, "explore/plan_trip.html")


def journeys(request):
    selected = request.GET.get("theme", "All")
    shown = TOURS if selected == "All" else [t for t in TOURS if t["tag"] == selected]
    return render(request, "explore/journeys.html", {"tours": shown, "selected": selected, "saved_slugs": saved(request)})


def tour_detail(request, slug):
    tour = find_tour(slug)
    itinerary = ["Arrive & settle into your first beautiful stay", "Travel deeper with your private guide", "A day designed around the landscape", "Unhurried moments and a memorable farewell"]
    return render(request, "explore/tour_detail.html", {"tour": tour, "itinerary": itinerary, "is_saved": slug in saved(request)})


def toggle_save(request, slug):
    find_tour(slug)
    saved_tours = saved(request)
    if slug in saved_tours:
        saved_tours.remove(slug)
        messages.info(request, "Removed from your wish list.")
    else:
        saved_tours.append(slug)
        messages.success(request, "Saved to your wish list.")
    request.session["saved_tours"] = saved_tours
    return redirect(request.META.get("HTTP_REFERER", "home"))


def inquire(request):
    if request.method == "POST":
        Inquiry.objects.create(name=request.POST["name"], email=request.POST["email"], travelers=request.POST.get("travelers", 2), travel_date=request.POST.get("travel_date") or None, message=request.POST.get("message", ""))
        messages.success(request, "Your travel designer will be in touch within one business day.")
    return redirect(request.META.get("HTTP_REFERER") or reverse("plan_trip"))


def transport(request):
    if request.method == "POST":
        TransportRequest.objects.create(
            name=request.POST["name"], email=request.POST["email"], pickup=request.POST["pickup"],
            destination=request.POST["destination"], pickup_date=request.POST["pickup_date"],
            pickup_time=request.POST.get("pickup_time") or None, passengers=request.POST.get("passengers", 2),
            notes=request.POST.get("notes", ""),
        )
        messages.success(request, "Transfer request received. We’ll confirm your driver and price shortly.")
        return redirect(request.META.get("HTTP_REFERER") or reverse("transport"))
    return render(request, "explore/transport.html")
