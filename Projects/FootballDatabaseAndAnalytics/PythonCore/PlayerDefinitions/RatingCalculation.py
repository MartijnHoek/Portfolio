from dataclasses import dataclass

@dataclass
class PositionRatings:
    """ Dataset defining all the possible positions """
    gk: int
    cb: int
    rb: int
    lb: int
    lwb: int
    rwb: int
    cdm: int
    cm: int
    lm: int
    rm: int
    cam: int
    cf: int
    lw: int
    rw: int
    st: int

class RatingCalculator:
    """ Class used for calculating ratings based on the values defined in a player object"""
    def __init__(self, physical_stats, mental_stats, technical_stats, goalkeeping_stats):
        """ Unpack all the stats and values from each dataset and create a self. variable from it
        these will be used to calculate the ratings easier """
        self.physical_stats = physical_stats
        self.mental_stats = mental_stats
        self.technical_stats = technical_stats
        self.goalkeeping_stats = goalkeeping_stats

        self.acceleration = self.physical_stats.acceleration
        self.agility = self.physical_stats.agility
        self.balance = self.physical_stats.balance
        self.jumping = self.physical_stats.jumping
        self.reactions = self.physical_stats.reactions
        self.sprint_speed = self.physical_stats.sprint_speed
        self.stamina = self.physical_stats.stamina
        self.strength = self.physical_stats.strength

        self.aggression = self.mental_stats.aggression
        self.att_positioning = self.mental_stats.att_positioning
        self.composure = self.mental_stats.composure
        self.interceptions = self.mental_stats.interceptions
        self.vision = self.mental_stats.vision

        self.ball_control = self.technical_stats.ball_control
        self.crossing = self.technical_stats.crossing
        self.curve = self.technical_stats.curve
        self.def_awareness = self.technical_stats.def_awareness
        self.dribbling = self.technical_stats.dribbling
        self.fk_accuracy = self.technical_stats.fk_accuracy
        self.finishing = self.technical_stats.finishing
        self.heading_accuracy = self.technical_stats.heading_accuracy
        self.long_pass = self.technical_stats.long_pass
        self.long_shots = self.technical_stats.long_shots
        self.penalties = self.technical_stats.penalties
        self.short_pass = self.technical_stats.short_pass
        self.shot_power = self.technical_stats.shot_power
        self.slide_tackle = self.technical_stats.slide_tackle
        self.stand_tackle = self.technical_stats.stand_tackle
        self.volleys = self.technical_stats.volleys

        self.gk_diving = self.goalkeeping_stats.gk_diving
        self.gk_handling = self.goalkeeping_stats.gk_handling
        self.gk_kicking = self.goalkeeping_stats.gk_kicking
        self.gk_positioning = self.goalkeeping_stats.gk_positioning
        self.gk_reflexes = self.goalkeeping_stats.gk_reflexes

        self.ratings = None

    def get_ratings(self):
        """ Function that calls each get_rating function per position
        :return: PostionRatings dataset containing the rating per position
        """
        self.ratings = PositionRatings(
            gk=self.get_rating_gk(),
            cb=self.get_rating_cb(),
            rb=self.get_rating_lb_rb(),
            lb=self.get_rating_lb_rb(),
            lwb=self.get_rating_lwb_rwb(),
            rwb=self.get_rating_lwb_rwb(),
            cdm=self.get_rating_cdm(),
            cm=self.get_rating_cm(),
            lm=self.get_rating_lm_rm(),
            rm=self.get_rating_lm_rm(),
            cam=self.get_rating_cam(),
            cf=self.get_rating_cf(),
            lw=self.get_rating_lw_rw(),
            rw=self.get_rating_lw_rw(),
            st=self.get_rating_st(),
        )
        return self.ratings

    def get_rating_gk(self):
        """ Get the rating for the GK position
        :return: round value GK rating
        """
        gk_rating = ((self.reactions * 0.11) + (self.gk_diving * 0.21) + (self.gk_handling * 0.21) + (self.gk_kicking * 0.05) +
                     (self.gk_positioning * 0.21) + (self.gk_reflexes * 0.21))

        return round(gk_rating)

    def get_rating_cb(self):
        """ Get the rating for the CB position
        :return: round value CB rating
        """
        cb_rating = ((self.aggression * 0.07) + (self.ball_control * 0.04) + (self.heading_accuracy * 0.1) + (self.interceptions * 0.13) +
                     (self.jumping * 0.03) + (self.def_awareness * 0.14) + (self.reactions * 0.05) + (self.short_pass * 0.05) +
                     (self.slide_tackle * 0.1) + (self.sprint_speed * 0.02) + (self.stand_tackle * 0.17) + (self.strength * 0.1))

        return round(cb_rating)

    def get_rating_lb_rb(self):
        """ Get the rating for the LB/RB position
        :return: round value LB/RB rating
        """
        lb_rb_rating = ((self.acceleration * 0.04) + (self.ball_control * 0.07) + (self.crossing * 0.09) + (self.heading_accuracy * 0.04) +
                        (self.interceptions * 0.12) + (self.def_awareness * 0.08) + (self.reactions * 0.08) + (self.short_pass * 0.07) +
                        (self.slide_tackle * 0.14) + (self.sprint_speed * 0.07) + (self.stamina * 0.08) + (self.stand_tackle * 0.11))

        return round(lb_rb_rating)

    def get_rating_lwb_rwb(self):
        """ Get the rating for the LWB/RWB position
        :return: round value LWB/RWB rating
        """
        lwb_rwb_rating = ((self.acceleration * 0.04) + (self.ball_control * 0.08) + (self.crossing * 0.12) + (self.dribbling * 0.04) +
                          (self.interceptions * 0.12) + (self.def_awareness * 0.07) + (self.reactions * 0.08) + (self.short_pass * 0.1) +
                          (self.slide_tackle * 0.11) + (self.sprint_speed * 0.06) + (self.stamina * 0.1) + (self.stand_tackle * 0.08))

        return round(lwb_rwb_rating)

    def get_rating_cdm(self):
        """ Get the rating for the CDM position
        :return: round value CDM rating
        """
        cdm_rating = ((self.aggression * 0.05) + (self.ball_control * 0.1) + (self.interceptions * 0.14) + (self.long_pass * 0.1) +
                      (self.def_awareness * 0.09) + (self.reactions * 0.07) + (self.short_pass * 0.14) + (self.slide_tackle * 0.05) +
                      (self.stamina * 0.06) + (self.stand_tackle * 0.12) + (self.strength * 0.04) + (self.vision * 0.04))

        return round(cdm_rating)

    def get_rating_cm(self):
        """ Get the rating for the CM position
        :return: round value CM rating
        """
        cm_rating = ((self.att_positioning * 0.06) + (self.ball_control * 0.14) + (self.dribbling * 0.07) + (self.finishing * 0.02) +
                     (self.interceptions * 0.05) + (self.long_pass * 0.13) + (self.long_shots * 0.04) + (self.reactions * 0.08) +
                     (self.short_pass * 0.17) + (self.stamina * 0.06) + (self.stand_tackle * 0.05) + (self.vision * 0.13))

        return round(cm_rating)

    def get_rating_cam(self):
        """ Get the rating for the CAM position
        :return: round value CAM rating
        """
        cam_rating = ((self.acceleration * 0.04) + (self.agility * 0.03) + (self.att_positioning * 0.09) + (self.ball_control * 0.15) +
                      (self.dribbling * 0.13) + (self.finishing * 0.07) + (self.long_pass * 0.04) + (self.long_shots * 0.05) +
                      (self.reactions * 0.07) + (self.short_pass * 0.16) + (self.sprint_speed * 0.03) + (self.vision * 0.14))

        return round(cam_rating)

    def get_rating_lm_rm(self):
        """ Get the rating for the LM/RM position
        :return: round value LM/RM rating
        """
        lm_rm_rating = ((self.acceleration * 0.07) + (self.att_positioning * 0.08) + (self.ball_control * 0.13) + (self.crossing * 0.1) +
                        (self.dribbling * 0.15) + (self.finishing * 0.06) + (self.long_pass * 0.05) + (self.reactions * 0.07) +
                        (self.short_pass * 0.11) + (self.sprint_speed * 0.06) + (self.stamina * 0.05) + (self.vision * 0.07))

        return round(lm_rm_rating)

    def get_rating_cf(self):
        """ Get the rating for the CF position
        :return: round value CF rating
        """
        cf_rating = ((self.acceleration * 0.05) + (self.att_positioning * 0.13) + (self.ball_control * 0.15) + (self.dribbling * 0.14) +
                     (self.finishing * 0.11) + (self.heading_accuracy * 0.02) + (self.long_shots * 0.04) + (self.reactions * 0.09) +
                     (self.short_pass * 0.09) + (self.shot_power * 0.05) + (self.sprint_speed * 0.05) + (self.vision * 0.08))

        return round(cf_rating)

    def get_rating_lw_rw(self):
        """ Get the rating for the LW/RW position
        :return: round value LW/RW rating
        """
        lw_rw_rating = ((self.acceleration * 0.07) + (self.agility * 0.03) + (self.att_positioning * 0.09) + (self.ball_control * 0.14) +
                        (self.crossing * 0.09) + (self.dribbling * 0.16) + (self.finishing * 0.1) + (self.long_shots * 0.04) +
                        (self.reactions * 0.07) + (self.short_pass * 0.09) + (self.sprint_speed * 0.06) + (self.vision * 0.06))

        return round(lw_rw_rating)

    def get_rating_st(self):
        """ Get the rating for the ST position
        :return: round value ST rating
        """
        st_rating = ((self.acceleration * 0.04) + (self.att_positioning * 0.13) + (self.ball_control * 0.1) + (self.dribbling * 0.07) +
                     (self.finishing * 0.18) + (self.heading_accuracy * 0.1) + (self.long_shots * 0.03) + (self.reactions * 0.08) +
                     (self.short_pass * 0.05) + (self.shot_power * 0.1) + (self.sprint_speed * 0.05) + (self.strength * 0.05) +
                     (self.volleys * 0.02))

        return round(st_rating)
