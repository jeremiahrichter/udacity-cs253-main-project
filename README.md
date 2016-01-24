# Udacity CS253 Main Project

This is a collection (among the various branches) of all of the various projects 
worked on as part of CS253, Udacity.com's Web Development course.

Branch listing:

*   **master**: This will house the code for the `wiki` final project, using the codebase  
    from the `blog` project built up through many of the lessons.
    
*   **lesson-2-archive**: A plurality of projects with handlers for `/` (day/month/year  
    validation), `/rot13` (testing escaping text and encoding with the ROT13 cipher),  
    and a simple `/signup` handler to redirect to a welcome page. These last two projects  
    are from Problem Set 2, but I wasn't separating branches well back then.

*   **lesson-3-archive**: Includes jinja2 templating from lesson 2a, this project intro-  
    duced the `AsciiChan` site using the GAE Datastore to store Art projects.
    
*   **problem-set-3**: This was the beginning of the `blog` codebase using the GAE Data-  
    store.
    
*   **lesson-4-archive**: No code changes introduces in this lesson, all changes were  
    done on the following test branch under a different codebase.
    
*   **temp-testing-base**: Created a new codebase without any of the handlers/models  
    from previous lessons: a clean web app.
    
*   **cookie-test**: Using `temp-testing-base`, worked on session persistence and hash-  
    ing for secure state information
    
*   **problem-set-4**: Merge hashing/secure cooking algorithms into the `blog` codebase  
    and addition of `/login`, `/logout` and `/signup` handlers

*   **lesson-5-archive**: Using `AsciiChan` base, added external API support from  
    [hostip.com](www.hostip.com) and [maps.google.com](maps.google.com) to add track-  
    ing of locations of the artists who contribute to the site.
    
*   **problem-set-5**: Jumping back to the `blog`, JSON support was added as an API for  
    the front page and each permalink post.
    
*   **lesson-6-archive**: Added GAE's support of memcache to the `AsciiChan` site.

*   **problem-set-6**: Added `memcache` to the `blog` web app; these cumulative  
    changes to `master`