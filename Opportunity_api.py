from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import (
    add_opportunity,
    create_table,
    delete_opportunity_by_title,
    filter_opportunities,
    get_all_opportunities,
    search_opportunities,
    update_opportunity_by_title,
)

app = FastAPI()
create_table()


class Opportunity(BaseModel):
    title: str
    category: str


@app.get("/")
def home():
    return {"message": "Welcome to Student Opportunity Finder"}


@app.get("/opportunities")
def list_opportunities():
    """Return every opportunity stored in the SQLite database."""
    return get_all_opportunities()


@app.get("/search")
def search_opportunity(search: str):
    """Search titles AND categories, case-insensitively."""
    return search_opportunities(search)


@app.get("/filter")
def filter_opportunity(category: str = "", title: str = ""):
    """Filter by category and/or title. Empty filters do not exclude anything."""
    return filter_opportunities(category, title)


@app.post("/opportunities")
def add_oppt(opportunity: Opportunity):
    """Insert a new opportunity and return it together with its generated id."""
    created = add_opportunity(opportunity.title, opportunity.category)

    return {
        "message": "Opportunity added successfully",
        "id": created["id"],
        "opportunity": created,
    }


@app.put("/opportunities/{opportunity_title}")
def update_Opport(
    opportunity_title: str,
    updated_data: Opportunity
):
    """Update the opportunity whose ORIGINAL title matches the path (case-insensitive)."""
    updated = update_opportunity_by_title(
        opportunity_title,
        updated_data.title,
        updated_data.category,
    )

    if updated is None:
        raise HTTPException(
            status_code=404,
            detail="Opportunity could not be found"
        )

    return {
        "message": "Opportunity updated successfully",
        "opportunity": updated,
    }


@app.delete("/opportunities/{opportunity_title}")
def delete_opportunity(opportunity_title: str):
    """Delete the opportunity whose title matches the path (case-insensitive)."""
    deleted = delete_opportunity_by_title(opportunity_title)

    if deleted is None:
        raise HTTPException(
            status_code=404,
            detail="Opportunity could not be found"
        )

    return {
        "message": "Opportunity deleted successfully",
        "opportunity": deleted,
    }
