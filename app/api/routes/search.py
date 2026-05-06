from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/search", tags=["Smart Search Demo"])


ITEMS = [
    {
        "name": "New Balance 990v6",
        "category": "Sneakers",
        "description": "Premium everyday sneaker with excellent comfort for long walks.",
        "tags": ["comfortable", "walking", "premium", "everyday", "sneakers"],
    },
    {
        "name": "ASICS Gel-Kayano",
        "category": "Sneakers",
        "description": "Supportive shoe for running and walking with strong stability.",
        "tags": ["supportive", "running", "walking", "stability", "sneakers"],
    },
    {
        "name": "Nike Vomero",
        "category": "Sneakers",
        "description": "Soft cushioned sneaker for daily comfort and long days on your feet.",
        "tags": ["soft", "cushioning", "walking", "comfortable", "sneakers"],
    },
    {
        "name": "Quiet Italian Restaurant in Soho",
        "category": "Restaurants",
        "description": "A quiet Italian dinner spot suitable for dates in central London.",
        "tags": ["quiet", "date", "italian", "london", "restaurant"],
    },
    {
        "name": "Affordable Studio Near University",
        "category": "Properties",
        "description": "Compact studio apartment close to university campuses and public transport.",
        "tags": ["affordable", "student", "university", "studio", "property"],
    },
]


class SearchRequest(BaseModel):
    query: str


@router.post("")
async def search(request: SearchRequest):
    words = request.query.lower().split()
    results = []

    for item in ITEMS:
        searchable = " ".join(
            [
                item["name"],
                item["category"],
                item["description"],
                " ".join(item["tags"]),
            ]
        ).lower()

        score = sum(1 for word in words if word in searchable)

        if score > 0:
            results.append({**item, "score": score})

    results.sort(key=lambda item: item["score"], reverse=True)

    return {"results": results}
