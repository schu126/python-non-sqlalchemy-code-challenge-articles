class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if isinstance (new_title, str) and 50 >= len(new_title) >= 5 and not hasattr (self, '_title'):
            self._title = new_title
        
class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str) and len(new_name) > 0 and not hasattr (self, '_name'):
            self._name = new_name

    def articles(self):
        result = []
        for article in Article.all:
            if article.author is self:
                result.append(article)
        return result

        # return [article for article in Article.all if article.author is self]

    def magazines(self):
        result = set()
        for article in Article.all:
            if article.author is self:
                result.add(article.magazine)
        return list(result)
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        magazines = self.magazines()
        if not magazines:
            return None
        return list(set(magazine.category for magazine in magazines))


class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
      
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance (new_name, str) and 16 >= len(new_name) >= 2:
            self._name = new_name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, new_category):
        if isinstance (new_category, str) and len(new_category) > 0:
            self._category = new_category

    def articles(self):
        return [article for article in Article.all if article.magazine is self]


    def contributors(self):
        result = set()
        for article in self.articles():
            result.add(article.author)
        return list(result)

    def article_titles(self):
        
        if len(self.articles()) == 0:
            return None
        
        title_list = []

        for article in self.articles(): 
            title_list.append(article.title)

        return title_list

    def contributing_authors(self):
        author_list = []
        for article in self.articles():
            author_list.append(article.author)

        result = []
        for author in author_list:
            if author_list.count(author) > 2:
                result.append(author)
        
        if len(result) > 0:
            return result
        else:
            return None

        # SHAN CODE
        # if len(self.articles()) <= 2:
        #     return None

        # author_dict = {}
        # for article in self.articles():
        #     if article.author in author_dict:
        #         author_dict[article.author] += 1
        #     else:
        #         author_dict[article.author] = 1
        
        # result = []
        # for author in author_dict:
        #     if author_dict[author] > 2:
        #         result.append(author)
        # return result