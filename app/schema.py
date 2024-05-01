import strawberry 
from typing import List
from . models import  BlogPost
from . types import BlogPostType

#query 
#GET or READ

@strawberry.type
class Query:
    @strawberry.field
    def blogposts(self,title:str=None) -> List[BlogPostType]:
        if title:
            blog = BlogPost.objects.filter(title=title)
            return blog
        return BlogPost.objects.all()




#Mutation
#Create, Update, Delete
#POST, PUT, PATCH, DELETE

@strawberry.type
class Mutation:
    @strawberry.field
    def create_blogpost(self, title: str, author: str, message: str) -> BlogPostType:
        blog = BlogPost(title=title, author=author, message=message)
        blog.save()
        return BlogPostType(
            id=blog.id,
            title=blog.title,
            author=blog.author,
            message=blog.message
        )
    
    @strawberry.field
    def update_blogpost(self, id:int, title:str, author:str, message:str) -> List[BlogPostType]:
        blog = BlogPost.objects.get(id=id)
        blog = BlogPost(title=title, author=author, message=message)
        blog.save()
        return blog

#Define A Schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
