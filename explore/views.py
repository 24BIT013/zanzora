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
        {"number": "01", "title": "A crossroads of the Indian Ocean", "copy": "Zanzibar’s story has always been connected to the sea. Swahili communities, African mainland networks, Arabian Peninsula traders, Indian merchants and later European powers all left an imprint on the islands. That exchange can still be felt in the language, cooking, faith, music and architecture of everyday life."},
        {"number": "02", "title": "Stone Town: living history", "copy": "Stone Town is more than a beautiful old quarter. Its dense lanes, coral-rag houses, carved doors, mosques, churches and shopfronts tell a layered story of Swahili coastal life and Indian Ocean commerce. UNESCO recognizes it as an outstanding Swahili trading town, shaped by African, Arab, Indian and European influences."},
        {"number": "03", "title": "The Omani era and the clove economy", "copy": "In the nineteenth century, Omani rulers and traders made Zanzibar an important political and commercial centre. Cloves became central to the island economy, and their perfume still rises from farms in the humid interior. A thoughtful spice tour is a good way to understand both the flavour and the difficult human history behind plantation agriculture."},
        {"number": "04", "title": "Remembering the slave trade", "copy": "Zanzibar was one of East Africa’s major slave-trading ports. This history deserves time, care and respect. The Anglican Cathedral in Stone Town stands at the site of the former final open slave market; visitors can learn from local historians and memorial sites rather than treating this chapter as a photo stop."},
        {"number": "05", "title": "Dhow craft and coastal knowledge", "copy": "The lateen-sailed dhow is a living symbol of the Swahili coast. For generations, sailors have read monsoon winds, currents and tides to connect island communities across the Indian Ocean. A sunset sail is lovely, but the deeper story is one of craftsmanship, navigation and trade."},
        {"number": "06", "title": "Taarab, ngoma and the night air", "copy": "Zanzibar’s soundscape carries poetry and memory. Taarab—a Swahili musical tradition associated with wedding celebrations—blends voices and instruments in richly expressive performances. Listen for it in cultural spaces and community events, alongside ngoma drumming and kidumbak rhythms."},
        {"number": "07", "title": "Food with many homes", "copy": "A Zanzibari table may bring together coconut, cassava, fresh fish, pilau rice, tamarind, cardamom, cloves and chilli. Try octopus curry, urojo soup, grilled seafood and fresh sugar-cane juice, and ask where ingredients come from. The best meals often begin with a market visit or a family recipe."},
        {"number": "08", "title": "Tides that reveal worlds", "copy": "On the east coast, the sea can move far beyond the reef at low tide, revealing sandbanks, sea grass and coral shallows. This rhythm shapes fishing, farming, beach walks and daily plans. Go with a local guide, respect marine life, and let the tide set the pace rather than fighting it."},
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
