from datetime import timedelta,date,datetime
from odoo import models, fields, api, exceptions
from dateutil.relativedelta import relativedelta

class Pelicula(models.Model):
    _name = 'pelicula.modelo'
    _description = "Modulo Pelicula"
    _inherit = 'base.empresa'

    name = fields.Char(string="Pelicula", required=True)
    responsible_id = fields.Many2one('res.users', ondelete='set null', string="Director", index=True)
    libros_ids = fields.One2many('libro.modelo', 'pelicula_id', string="Libro")
    description = fields.Text(string="Descripcion")
    actores = fields.Integer(string="Number of actores")
    librosPelicula = fields.Many2many('libro.modelo', 'event_visita', 'pelicula_id', 'libros_id', 'Libros')
   

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copia de {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copia de {}".format(self.name)
        else:
            new_name = u"Copia de {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Pelicula, self).copy(default)

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "El nombre del equipo no puede ser el mismo que la descripcion"),

        ('name_unique',
         'UNIQUE(name)',
         "Ya existe un equipo con este nombre!"),
    ]

    @api.onchange('actores')
    def _verify_valid_actores(self):
        if self.actores < 0:
            return {
                'warning': {
                    'title': "Incorrect 'seats' value",
                    'message': "The number of available actores may not be negative",
                },
            }

class Libro(models.Model):
    _name = 'libro.modelo'
    _description = "Modulo Libro"

    name = fields.Char(required=True, string="Libro")
    start_date = fields.Date(string="Fecha de salida", default=fields.Date.today)
    fecha_salida = fields.Date()
    #end_date = fields.Date(string="Fecha de despedida", store=True, compute='_get_end_date', inverse='_set_end_date')
    #duration = fields.Float(digits=(6, 2), help="Duration in days", string="Tiempo en el equipo")
    #goals = fields.Integer(string="Numero de goles")
    #active = fields.Boolean(default=True, string="Actualmente en el equipo")
    libreria = fields.Boolean(default=True, string="En librerias")
    venta = fields.Selection([('si', 'Si'),('no','No')],default='no', string="A la venta?")
    # instructor_id = fields.Many2one('res.partner', string="Entrenador")
    pelicula_id = fields.Many2one('pelicula.modelo', ondelete='cascade', string="Equipo", required=True)
    peliculasLibro = fields.Many2many('pelicula.modelo', 'event_visita', 'pelicula_id', 'libros_id', 'Peliculas')
    #average_ids = fields.Many2many('res.partner', string="Objetivo Goles")
    #scored_goals = fields.Float(string="Objetivo de goles", compute='_scored_goals')

    #hours = fields.Float(string="Duration in hours",compute='_get_hours', inverse='_set_hours')

    # @api.depends('goals', 'average_ids')
    # def _scored_goals(self):
    #     for r in self:
    #         if not r.goals:
    #             r.scored_goals = 0.0
    #         else:
    #             r.scored_goals = 100.0 * len(r.average_ids) / r.goals


    # @api.depends('start_date', 'duration')
    # def _get_end_date(self):
    #     for r in self:
    #         if not (r.start_date and r.duration):
    #             r.end_date = r.start_date
    #             continue

    #         # Add duration to start_date, but: Monday + 5 days = Saturday, so
    #         # subtract one second to get on Friday instead
    #         duration = timedelta(days=r.duration, seconds=-1)
    #         r.end_date = r.start_date + duration

    # def _set_end_date(self):
    #     for r in self:
    #         if not (r.start_date and r.end_date):
    #             continue

    #         # Compute the difference between dates, but: Friday - Monday = 4 days,
    #         # so add one day to get 5 days instead
    #         r.duration = (r.end_date - r.start_date).days + 1

    # @api.depends('duration')
    # def _get_hours(self):
    #     for r in self:
    #         r.hours = r.duration * 24

    # def _set_hours(self):
    #     for r in self:
    #         r.duration = r.hours / 24




#te comento esto crea dos modelos heredados. Para mostrarlos en el menu y demas como pelis y libros. 
#para poder llamar a estos modelos y demas tienes q irte al __manifest__.py y en depends creo q es poner el nombre de los modulos base y baseModule (puedes llamar al que quieras)
#una vez q hayas entendido esto sube hasta la clase Pelicula veras que hay otra _inherit. basicamente donde pases eso podras coger los campos de esa clase heredada
#en el ir.actions.act_window de extender fijate en la diferencia con el de heredar
 
class Heredar(models.Model):
    #este va a tener datos de el modulo base concretamente de su clase empresa. COge sus datos 
    #de esta manera crea una tabla nueva que se llamara como el _name
    _name = 'multimedia.heredar'
    _inherit = 'base.empresa'
    #codigoPostal = fields.Char(string="codigo postal")

class Extender(models.Model):
    #NO se crea una tabla nueva en la base de datos
    _inherit = 'base.empresa'
    #dni = fields.Char(string="dni")