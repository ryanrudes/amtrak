from enum import Enum

"""
ADULT
 * Age: 16+
 * Discount: Full standard fare
 * Restrictions: None
    
SENIOR
 * Age: 65+ (Amtrak) / 60+ (VIA Rail Canada)
 * Discount: 10%
 * Restrictions
    - Not valid on some connecting Amtrak Thruway services.
    - Does not apply to non-Acela Business Class, First Class or sleeper accommodation charges.

Youth
 * Age: 13 - 15
 * Discount: Full standard fare
 * Restrictions
    - Must be accompanied by at least one adult (18+) in the same reservation.
    - Call 1-800-USA-RAIL to make reservations for unaccompanied youth.
    
Child
 * Age: 2 - 12
 * Discount: 50%
 * Restrictions
    - Must be accompanied by at least one adult (18+) in the same reservation.
    - Not valid for weekday Acela travel.
    - Not valid on some connecting Amtrak Thruway services.
    - Does not apply to non-Acela Business Class, First Class or sleeper accommodation charges.

INFANT
 * Age: Under 2
 * Discount: Free / 50%
 * Restrictions
    - Must be accompanied by at least one adult (18+) in the same reservation.
    - One infant may ride free with each passsenger paying an adult fare.
    - Additional infants (more infants than adults) receive 50% child discount and can occupy a seat.
    - Not valid for weekday Acela travel.
    - Not valid on some connecting Amtrak Thruway services.
    - Does not apply to non-Acela Business Class, First Class or sleeper accommodation charges.

MILITARY
 * Age: 18+
 * Discount: 10%
 * Restrictions
    - Active duty U.S. military personnel and spouses.
    - Not valid on some connecting Amtrak Thruway services.
    - Not valid on the Canadian portion of services operated jointly by Amtrak and VIA Rail Canada.
    - Does not apply to non-Acela Business Class, First Class or sleeper accommodation charges.
    - Must present valid Military ID or valid documentation to the conductor at the time of ticket collection.
    
MILITARY_DEPENDENT
 * Age: 2 - 12
 * Discount: 10% in addition to child 50% discount
 * Restrictions
    - Dependent of active duty U.S. military personnel.
    - Must be accompanied by at least one adult (18+) in the same reservation.
    - Not valid on some connecting Amtrak Thruway services.
    - Not valid on the Canadian portion of services operated jointly by Amtrak and VIA Rail Canada.
    - Does not apply to non-Acela Business Class, First Class or sleeper accommodation charges.
    
ADULT_WITH_DISABILITY
 * Age: 18+
 * Discount: 10%; 50% on Downeaster services (Boston, MA to Portland, ME).
 * Restrictions 
    - On the Auto Train, only passengers traveling with their own wheeled mobility device (wheelchair or scooter) qualify for the passengers with disability discount.

CHILD_WITH_DISABILITY
 * Age: 2 - 12
 * Discount: 10% in addition to child 50% discount
 * Restrictions
    - Must be accompanied by at least one adult (18+) in the same reservation.
    - On the Auto Train, only passengers traveling with their own wheeled mobility device (wheelchair or scooter) qualify for the passengers with disability discount.

COMPANION
 * Age: 13+
 * Discount: 10%
 * Restrictions 
    - Must be booked with Passenger with a Disability traveler.

RAIL_PASSENGERS_ASSOCIATION
 * Age: 13+
 * Discount: 10%
 * Restrictions
    - Three-day advanced purchase for all travel.
    - Not valid on some connecting Amtrak Thruway services.
    - Not valid on the Canadian portion of services operated jointly by Amtrak and VIA Rail Canada.
    - Does not apply to non-Acela Business Class, First Class or sleeper accommodation charges.
    - Must present a valid membership card at time of travel.

VETERAN
 * Age: 18+
 * Discount: 10%
 * Restrictions
    - U.S. military veteran only (Army, Navy, Air Force, Marine Corps, Coast Guard, Space Force and only commissioned officers from NOAA Corps, U.S. Public Health Service, U.S. Merchant Marine) with a valid military veteran identification card. 
    - Not valid on some connecting Amtrak Thruway services.
    - Not valid on the Canadian portion of services operated jointly by Amtrak and VIA Rail Canada.
    - Does not apply to non-Acela Business Class, First Class or sleeper accommodation charges.
    - Does not apply to dependents.
"""
class Discount(Enum):
    """Enum representing different discount categories for train travelers.
    
    Attributes:
        ADULT: Discount category for adults (age 16+).
        SENIOR: Discount category for seniors (age 65+).
        YOUTH: Discount category for youths (age 13-15).
        CHILD: Discount category for children (age 2-12).
        INFANT: Discount category for infants (under 2).
        MILITARY: Discount category for active duty U.S. military personnel and spouses.
        MILITARY_DEPENDENT: Discount category for dependents of active duty U.S. military personnel.
        ADULT_WITH_DISABILITY: Discount category for adults with disabilities.
        CHILD_WITH_DISABILITY: Discount category for children with disabilities.
        COMPANION: Discount category for companions traveling with passengers with disabilities.
        RAIL_PASSENGERS_ASSOCIATION: Discount category for members of the Rail Passengers Association.
        VETERAN: Discount category for U.S. military veterans.
    
    Notes:
        - Certain discounts may have additional restrictions and eligibility criteria.
        - Discounts may not be applicable to all types of train services or accommodations.
        - Customers are advised to check eligibility and restrictions before booking.
    """
    ADULT = "Adult"
    SENIOR = "Senior"
    YOUTH = "Youth"
    CHILD = "Child"
    INFANT = "Infant"
    MILITARY = "Military"
    MILITARY_DEPENDENT = "Military Dependent"
    ADULT_WITH_DISABILITY = "Adult With Disability"
    CHILD_WITH_DISABILITY = "Child With Disability"
    COMPANION = "Companion"
    RAIL_PASSENGERS_ASSOCIATION = "Rail Passengers Association"
    VETERAN = "Veteran"