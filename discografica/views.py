from .forms import *
from .models import *
from django.shortcuts import get_object_or_404
from django.shortcuts import render
import json
from django.http import *
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

LOAD_PAGINATION_ITEMS = 6


def index(request):
    p = Publicacion.objects.all()
    return render(request, 'discografica/home.html',
                  {'publicaciones': p.order_by("-upload_date")[:LOAD_PAGINATION_ITEMS],
                   'destacado': p.order_by("-visitas")[:5],
                   'data_size': LOAD_PAGINATION_ITEMS})


def loadPagina(request, n):
    response = {}

    response["ok"] = False
    response["item"] = 0
    response["more"] = False
    response["content"] = ''

    n = int(n)
    n2 = n + LOAD_PAGINATION_ITEMS
    response["size"] = n2

    publicaciones = Publicacion.objects.all().order_by("-upload_date")
    length = publicaciones.count()
    i = 0
    for publicacion in publicaciones[n:n2]:
        response["content"] += '' \
                               '<a class="home-box fade" href="/letra/' + str(
            publicacion.id) + '/" style="text-decoration: none;">' \
                              '' \
                              '<div class="row-fluid img-album">' \
                              '' \
                              ' <img class="img-album-in" ' \
                              'src="' + str(
            publicacion.album.imagen) + '" ' \
                                        'alt="' + publicacion.album.titulo + '" ' \
                                                                             'title="' + publicacion.album.titulo + '"/>' \
                                                                                                                    '' \
                                                                                                                    '</div>' \
                                                                                                                    '' \
                                                                                                                    '<div class="row-fluid">' \
                                                                                                                    '<div class="col-md-12" style="padding: 10px;">' \
                                                                                                                    '<div class="home-box-datos home-box-c">' + publicacion.cancion.titulo + '</div>' \
                                                                                                                                                                                             '<div class="home-box-datos home-box-a">' + publicacion.album.artista.nombre + '</div>' \
                                                                                                                                                                                                                                                                            '</div>' \
                                                                                                                                                                                                                                                                            '</div>' \
                                                                                                                                                                                                                                                                            '' \
                                                                                                                                                                                                                                                                            '</a>'

        i += 1

    if i != 0:
        response["ok"] = True
        response["item"] = i

    if n2 < length:
        response["more"] = True

    return HttpResponse(json.dumps(response), content_type='application/json')


def letra(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)
    publicacion.visitas += 1
    publicacion.save()

    return render(request, 'discografica/letra.html', {'publicacion': publicacion,
                                                       'canciones': Publicacion.objects.filter(
                                                           album_id=publicacion.album.id),
                                                       'albumes': Album.objects.filter(
                                                           artista_id=publicacion.album.artista.id),
                                                       'alid': publicacion.album.id,
                                                       'cid': publicacion.cancion.id, })


@login_required(login_url='/login/')
def panel_action(request):
    if request.method == 'POST':

        if request.POST["is_artista"] == "0":
            if Artista.objects.filter(nombre=request.POST["artista_nombre"]).count() == 0:
                artista = Artista(
                    nombre=str(request.POST["artista_nombre"]).title()
                )
                artista.save()
                arid = artista.id
            else:
                arid = Artista.objects.get(nombre=request.POST["artista_nombre"]).id
        else:
            arid = request.POST["is_artista"]

        if request.POST["is_album"] == "0":
            album_img = addImgAlbum(request.POST, request.FILES)
            if album_img.is_valid():
                album = Album(
                    artista_id=arid,
                    titulo=str(request.POST['album_titulo']).capitalize(),
                    fecha=request.POST['album_fecha'],
                    imagen=album_img.cleaned_data['imagen'],
                )
            else:
                album = Album(
                    artista_id=arid,
                    titulo=str(request.POST['album_titulo']).capitalize(),
                    fecha=request.POST['album_fecha'],
                )

            album.save()

            alid = album.id
        else:
            alid = request.POST["is_album"]

        if request.POST["is_cancion"] == "0":
            cancion = Cancion(
                titulo=str(request.POST['cancion_titulo']).capitalize(),
                letra=request.POST['cancion_letra'],
            )

            cancion.save()

            cid = cancion.id
        else:
            cid = request.POST["is_cancion"]

        if Publicacion.objects.filter(album_id=alid, cancion_id=cid).count() == 0:
            publicacion = Publicacion(
                album_id=alid,
                cancion_id=cid
            )

            publicacion.save()

    return HttpResponseRedirect('/')

    # return HttpResponse(json.dumps(response), content_type='application/json')


@login_required(login_url='/login/')
def panel(request):
    return render(request, 'discografica/panel.html',
                  {'artistas': Artista.objects.all(),
                   'albumes': Album.objects.all(),
                   'canciones': Cancion.objects.all(),
                   'imagen': addImgAlbum()})


@login_required(login_url='/login/')
def form_artista(request):
    response = {}

    response["ok"] = False
    response["item"] = 0
    response["content"] = ''

    if len(request.GET["s"]) == 1:
        artistas = Artista.objects.filter(nombre__istartswith=request.GET["s"])[:4]
    else:
        artistas = Artista.objects.filter(nombre__icontains=request.GET["s"])[:4]

    for artista in artistas:
        if len(request.GET["s"]) == 1:
            nombre = "{}{}".format("<span style='font-weight: 500;'>" + request.GET["s"].lower() + "</span>",
                                   artista.nombre[1:].lower())
        else:
            nombre = artista.nombre.lower().replace(request.GET["s"].lower(),
                                                    "<span style='font-weight: 500;'>" + request.GET[
                                                        "s"].lower() + "</span>")

        response["content"] += '<li>' \
                               '<button class="btn btn-link btn-block form-autocomplete-item" style="outline: none; text-decoration: none;" data-artista-nombre="' + artista.nombre + '" data-artista-id="' + str(
            artista.id) + '">' + nombre + '</button>' \
                                          '</li>'
    if artistas.count() != 0:
        response["ok"] = True
        response["item"] = artistas.count()

    return HttpResponse(json.dumps(response), content_type='application/json')


@login_required(login_url='/login/')
def form_album(request):
    response = {}

    response["ok"] = False
    response["item"] = 0
    response["content"] = ''

    albumes = Album.objects.filter(artista_id=request.GET["id"])

    for album in albumes:
        response["content"] += '' \
                               '<div class="home-box form-album-box" data-album-id="' + str(
            album.id) + '" data-album-titulo="' + album.titulo + '" style="text-decoration: none;">' \
                                                                 '' \
                                                                 '<div class="row-fluid img-album">' \
                                                                 '' \
                                                                 ' <img class="form-album-box-img" ' \
                                                                 'src="/' + str(
            album.imagen) + '" ' \
                            'alt="' + album.titulo + '" ' \
                                                     'title="' + album.titulo + '"/>' \
                                                                                '' \
                                                                                '</div>' \
                                                                                '' \
                                                                                '<div class="row-fluid">' \
                                                                                '<div class="col-md-12" style="padding: 10px;">' \
                                                                                '<div class="home-box-datos home-box-c">' + album.titulo + '</div>' \
                                                                                                                                           '<div class="home-box-datos home-box-a">' + str(
            album.fecha) + '</div>' \
                           '</div>' \
                           '</div>' \
                           '' \
                           '</div>'

    if albumes.count() != 0:
        response["ok"] = True
        response["item"] = albumes.count()

    return HttpResponse(json.dumps(response), content_type='application/json')


@login_required(login_url='/login/')
def form_cancion(request):
    response = {}

    response["ok"] = False
    response["item"] = 0
    response["content"] = ''

    if len(request.GET["s"]) == 1:
        canciones = Cancion.objects.filter(titulo__istartswith=request.GET["s"])[:4]
    else:
        canciones = Cancion.objects.filter(titulo__icontains=request.GET["s"])[:4]

    for cancion in canciones:

        if len(request.GET["s"]) == 1:
            titulo = "{}{}".format("<span style='font-weight: 500;'>" + request.GET["s"].lower() + "</span>",
                                   cancion.titulo[1:].lower())
        else:
            titulo = cancion.titulo.lower().replace(request.GET["s"].lower(),
                                                    "<span style='font-weight: 500;'>" + request.GET[
                                                        "s"].lower() + "</span>")

        response["content"] += '<li>' \
                               '<button class="btn btn-link btn-block form-autocomplete-item" style="outline: none; text-decoration: none;" data-cancion-titulo="' + cancion.titulo + '" data-cancion-id="' + str(
            cancion.id) + '">' + titulo + '</button>' \
                                          '</li>'

    if canciones.count() != 0:
        response["ok"] = True
        response["item"] = canciones.count()
        response["letra"] = cancion.letra

    return HttpResponse(json.dumps(response), content_type='application/json')


@login_required(login_url='/login/')
def form_check(request):
    response = {}

    response["ok"] = True

    if request.GET["alid"] != "0" and request.GET["cid"] != "0":
        publicaciones = Publicacion.objects.filter(album_id=request.GET["alid"],
                                                   cancion_id=request.GET["cid"])
        if publicaciones.count() != 0:
            response["ok"] = False

    return HttpResponse(json.dumps(response), content_type='application/json')


def album(request, id_album):
    response = {}

    response["ok"] = False
    response["item"] = 0
    response["content"] = ''

    publicaciones = Publicacion.objects.filter(album=id_album)

    i = 0

    for publicacion in publicaciones:
        response["content"] += '<a href="/letra/' + str(publicacion.id) + '" class="album-box-canciones-item">' \
                                                                          '' + publicacion.cancion.titulo + '</a>'

        i += 1

    if i != 0:
        response["ok"] = True
        response["item"] = i

    return HttpResponse(json.dumps(response), content_type='application/json')


def login_user(request):
    logout(request)

    username = password = ''
    error = ''

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(request.POST.get('next', '/'))
        else:
            username = password = ''
            error = "Error al introducir los datos"

    return render_to_response('discografica/login.html',
                              {'error': error,
                               'next': request.GET['next'] if request.GET and 'next' in request.GET else ''},
                              context_instance=RequestContext(request))
